import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.core.config import settings

from app.repositories.document_repo import create_document

def upload_document(db: Session, tenant_id: int, title: str, file: UploadFile):

    upload_dir = Path(settings.UPLOAD_DIR)

    upload_dir.mkdir(exist_ok=True)

    unique_filename = f"{uuid4()}-{file.filename}"

    file_path = upload_dir/unique_filename

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    document = create_document(db=db,tenant_id=tenant_id,title=title,filepath=str(file_path))

    return document