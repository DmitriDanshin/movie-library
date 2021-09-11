from fastapi import APIRouter

from . import (
    movies,
    genres
)

router = APIRouter()
router.include_router(movies.router)
router.include_router(genres.router)
