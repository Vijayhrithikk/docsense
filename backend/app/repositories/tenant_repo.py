from sqlalchemy.orm import Session

from app.models.tenant_model import Tenant

def create_tenant(db: Session, name: str) -> Tenant:
    tenant = Tenant(name=name)
    db.add(tenant)
    db.commit()
    db.refresh(tenant)

    return tenant

def get_tenant(db: Session, tenant_id: int):

    return db.query(Tenant).filter(Tenant.id==tenant_id).first()

def list_tenants(db: Session):
    return db.query(Tenant).all()
