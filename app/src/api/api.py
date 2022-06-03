from src.api.endpoints import login, users, items, lieux,categories, themes, ratings
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.core.config import settings
from fastapi.staticfiles import StaticFiles

api = FastAPI()

api.mount("/static", StaticFiles(directory="static"), name="static")

@api.get("/")
def read_root():
    return {"message": "Welcome to Projet 1CS backend"}



# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    api.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
api.include_router(login.router, tags=["login"])
api.include_router(users.router, prefix="/users", tags=["users"])
api.include_router(items.router, prefix="/items", tags=["items"])
api.include_router(lieux.router, prefix="/lieux", tags=["lieux"])
api.include_router(categories.router, prefix="/categories", tags=["categories"])
api.include_router(themes.router, prefix="/themes", tags=["themes"])
api.include_router(ratings.router, prefix="/ratings", tags=["ratings"])