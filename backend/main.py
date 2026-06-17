from fastapi import FastAPI
import app.models

from app.api.tenant_routes import router as tenant_router
from app.api.document_routes import router as document_router
from app.api.question_routes import router as question_router
from app.api.eval_router import (
    router as evaluation_router
)
from app.api.analytics_router import router as analytics_router
from app.api.health_router import router as health_router
from app.api.metrics_router import router as metrics_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://13.204.63.146"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(tenant_router)
app.include_router(document_router)
app.include_router(question_router)
app.include_router(evaluation_router)
app.include_router(analytics_router)
app.include_router(health_router)
app.include_router(metrics_router)
