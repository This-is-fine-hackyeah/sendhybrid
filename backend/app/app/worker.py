import zipfile
import requests
from glob import glob
from contextlib import contextmanager
import subprocess
from tempfile import TemporaryFile, NamedTemporaryFile, TemporaryDirectory
from raven import Client

from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError
from app.core.celery_app import celery_app
from app.core.config import settings
from app.core.security import create_access_token
from app import schemas, crud
from app.api import deps
from app.schemas import ConvertableFormats

client_sentry = Client(settings.SENTRY_DSN)

get_db = contextmanager(deps.get_db)


@celery_app.task(acks_late=True)
def test_celery(word: str) -> str:
    return f"test task return {word}"

def is_pdf(filename: str, content_type: str) -> bool:
    """Check if file is a real PDF a nie jakiś podrabianiec"""
    if content_type != "application/pdf":
        return False

    if not filename.endswith(".pdf"):
        return False
    return True

@celery_app.task(acks_late=True)
def check_file_type(document_data: dict):
    document = schemas.Document(**document_data)
    if is_pdf(document.filename, document.content_type):
        celery_app.send_task("app.worker.validate_pdf", args=[document.id, document.owner_id])
        return

    stem, ext = document.filename.rsplit(".", maxsplit=1)
    if ext in {
            ConvertableFormats.PPTX,
            ConvertableFormats.ODT,
            ConvertableFormats.XLS,
            ConvertableFormats.DOCX,
    }:
        celery_app.send_task("app.worker.convert_libreoffice", args=[document.id, document.owner_id])
        return

    if ext == ConvertableFormats.ZIP:
        celery_app.send_task("app.worker.extract_zip", args=[document.id, document.owner_id])
        return

    with get_db() as db:
        crud.document.mark_failed(db, validator_name="format", obj_in=document)


@celery_app.task(acks_late=True)
def validate_pdf(document_id: int, owner_id: int):
    return
    #with NamedTemporaryFile() as f:
        #download_file(document_id, owner_id, f)


def download_file(document_id: int, owner_id: int, fout: "file"):
    token = create_access_token(owner_id)
    headers = {"Authorization": f"Bearer {token}"}
    url = f"http://backend{settings.API_V1_STR}/documents/{document_id}/download"
    with requests.get(url, stream=True, headers=headers) as r:
        r.raise_for_status()
        for chunk in r.iter_content(chunk_size=8192):
            fout.write(chunk)

def upload_file(document_id: int, owner_id: int, fpath: str):
    token = create_access_token(owner_id)
    headers = {"Authorization": f"Bearer {token}"}
    url = f"http://backend{settings.API_V1_STR}/documents/{document_id}/upload"
    files = {'file': open(fpath, "rb")}
    r = requests.put(url, files=files, headers=headers)
    r.raise_for_status()

@celery_app.task(acks_late=True)
def convert_libreoffice(document_id: int, owner_id: int):
    with NamedTemporaryFile() as f, TemporaryDirectory() as tmpdir:
        download_file(document_id, owner_id, f)
        cmd = f"lowriter --headless --convert-to pdf {f.name} --outdir {tmpdir}"
        subprocess.run(cmd, shell=True)
        upload_file(document_id, owner_id, glob(f"{tmpdir}/*.pdf").pop())

@celery_app.task(acks_late=True)
def extract_zip(document_id: int, owner_id: int):
    with NamedTemporaryFile() as f, TemporaryDirectory() as tmpdir:
        download_file(document_id, owner_id, f)
        with zipfile.ZipFile(f, 'r') as zip_file:
            zip_file.extractall(tmpdir)
        upload_file(document_id, owner_id, glob(f"{tmpdir}/*.pdf").pop())

