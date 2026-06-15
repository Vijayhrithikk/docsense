from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.analytics_schema import (
    AnalyticsResponse,
)

from app.services.analytics_service import (
    AnalyticsService,
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)

service = AnalyticsService()


@router.get("/summary",response_model=AnalyticsResponse)
def get_summary(
    tenant_id: int,
    db: Session = Depends(get_db),
):

    return (service.get_summary(db=db,tenant_id=tenant_id))