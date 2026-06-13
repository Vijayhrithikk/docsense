from fastapi import (
    Depends,
    APIRouter,
    UploadFile,
    File,
    Form
)

from fastapi import BackgroundTasks

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.document import DocumentResponse


from app.services import document_service

router = APIRouter(prefix="/documents",tags=["documents"])

@router.post("",response_model=DocumentResponse)
def create_document(
    background_tasks: BackgroundTasks,
    tenant_id: int = Form(...),
    title:str = Form(...),
    file: UploadFile= File(...),
    
    db: Session = Depends(get_db),
):
    document = document_service.upload_document(db=db,tenant_id=tenant_id,title=title,file=file)
    document_id = document.id

    background_tasks.add_task(document_service.process_document, document_id)

    return document









    




    