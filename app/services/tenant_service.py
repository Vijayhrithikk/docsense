from sqlalchemy.orm import Session

from app.repositories.tenant_repo import (
    create_tenant,
    get_tenant,
    list_tenants
)

def onboard_tenant(db: Session, name: str):
    return create_tenant(db=db,name=name)

def get_tenants(db: Session,tenant_id: int):

    return get_tenant(db=db,tenant_id=tenant_id)

def fetch_tenants(db: Session):

    return list_tenants(db=db)