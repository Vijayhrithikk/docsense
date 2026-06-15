from fastapi import(
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.tenant import (
    TenantCreate,
    TenantResponse
)

from app.services.tenant_service import (
    onboard_tenant,
    fetch_tenants

)

router = APIRouter(prefix="/tenants",tags=["tenants"])

@router.post("",response_model=TenantResponse)
def create_tenant(payload: TenantCreate, db: Session= Depends(get_db)):

    return onboard_tenant(db=db, name=payload.name)

@router.get("", response_model=list[TenantResponse])
def list_all_tenants(db: Session= Depends(get_db)):

    return fetch_tenants(db=db)