from src.api.endpoints import login, users, items, lieux,categories, themes
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.core.config import settings

api_router = FastAPI()

@api_router.get("/")
def read_root():
    return {"message": "Welcome to Projet 1CS backend"}



# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    api_router.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(lieux.router, prefix="/lieux", tags=["lieux"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(themes.router, prefix="/themes", tags=["themes"])