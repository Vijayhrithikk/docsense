from fastapi import FastAPI

from app.api.tenant_routes import router as tenant_router
from app.api.document_routes import router as document_router

app = FastAPI()

app.include_router(tenant_router)
app.include_router(document_router)
