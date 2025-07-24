from fastapi import FastAPI
from app.api.v1.routes import auth

from app.db.base import Base
from app.db.session import engine  # adjust import if needed
from app.db.models import user
 
app = FastAPI(
    title="My FastAPI Project",
    description="API docs with Swagger UI",
    version="1.0.0",
    docs_url="/api/v1/docs",
    openapi_url="/api/v1/openapi.json"  
)
Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
