from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.metrics.service import (
    MetricsService,
)

from app.schemas.metrics_schema import (
    MetricsResponse,
)

router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"],
)

service = MetricsService()


@router.get("",response_model=MetricsResponse,)
def get_metrics(db: Session = Depends(get_db)):

    return (
        service.get_metrics(db=db)
    )