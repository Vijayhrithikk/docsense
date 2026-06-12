from fastapi import (
    Depends,
    APIRouter,
    UploadFile,
    File,
    Form
)

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.document import DocumentResponse

from app.services.document_service import upload_document

router = APIRouter(prefix="/documents",tags=["documents"])

@router.post("",response_model=DocumentResponse)
def create_document(
    tenant_id: int = Form(...),
    title:str = Form(...),
    file: UploadFile= File(...),
    db: Session = Depends(get_db)
):
    return upload_document(db=db,tenant_id=tenant_id,title=title,file=file)