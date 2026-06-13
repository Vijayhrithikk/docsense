import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile
from sqlalchemy.orm import Session
from app.db.database import SessionLocal

from app.core.config import settings

from app.repositories.document_repo import (
    create_document,
    get_document,
    update_document_error,
    update_document_status
)

from app.repositories.document_page_repo import bulk_create_pages

from app.processors.processor_factory import get_processor


def upload_document(db: Session, tenant_id: int, title: str, file: UploadFile):

    upload_dir = Path(settings.UPLOAD_DIR)

    upload_dir.mkdir(exist_ok=True)

    unique_filename = f"{uuid4()}-{file.filename}"

    file_path = upload_dir/unique_filename

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    document = create_document(db=db,tenant_id=tenant_id,title=title,filepath=str(file_path))

    return document


def process_document(document_id: int):

    
    db =  SessionLocal()
    try:
        
        document = get_document(db=db,document_id=document_id)

        if not document:
            raise ValueError("Document not found")
        
        update_document_status(db=db,document_id=document_id,status="processing")

        processor = get_processor(file_path=str(document.file_path))

        pages = processor.extract_text(file_path=str(document.file_path))

        if not pages:
            raise ValueError("No text extracted")

        bulk_create_pages(db=db,document_id=document_id,pages=pages)

        update_document_status(db=db,document_id=document_id,status="indexed")

    except Exception as e:

        update_document_status(db=db,document_id=document_id,status="failed")

        update_document_error(db=db,document_id=document_id,error_message=str(e))

    finally:
        db.close()


