import requests
from glob import glob
import subprocess
from tempfile import TemporaryFile, NamedTemporaryFile, TemporaryDirectory
from raven import Client

from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError
from app.core.celery_app import celery_app
from app.core.config import settings
from app.core.security import create_access_token
from app import schemas, crud
from app.schemas import ConvertableFormats

client_sentry = Client(settings.SENTRY_DSN)


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
    if not is_pdf(document.filename, document.content_type):
        pass

    stem, ext = document.filename.rsplit(".", maxsplit=1)
    if ext in {
            ConvertableFormats.PPTX,
            ConvertableFormats.ODT,
            ConvertableFormats.XLS,
            ConvertableFormats.DOCX,
    }:
        celery_app.send_task("app.worker.convert_libreoffice", args=[document.id, document.owner_id])


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
