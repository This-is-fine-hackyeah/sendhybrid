import requests
from tempfile import TemporaryFile
from raven import Client

from app.core.celery_app import celery_app
from app.core.config import settings
from app.core.security import create_access_token
from app import schemas, crud

client_sentry = Client(settings.SENTRY_DSN)


@celery_app.task(acks_late=True)
def test_celery(word: str) -> str:
    return f"test task return {word}"

@celery_app.task(acks_late=True)
def check_file_type(document_data: dict) -> str:
    """Check if file is a real PDF a nie jakiś podrabianiec"""
    document = schemas.Document(**document_data)
    if document.content_type != "application/pdf":
        # Can be converted else EOT
        pass

    # Check magic number:
    #

    token = create_access_token(document.owner_id)
    headers = {"Authorization": f"Bearer {token}"}
    url = f"http://backend{settings.API_V1_STR}/documents/{document.id}/download"
    with requests.get(url, stream=True, headers=headers) as r:
        r.raise_for_status()
        with TemporaryFile() as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

            # Do processing
    return ""
