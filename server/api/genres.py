from typing import List

from fastapi import APIRouter, Depends

from server.models.genres import Genre, GenreCreate
from server.services.genres import GenreService

router = APIRouter(
    prefix='/genres',
)


@router.get('/', response_model=List[Genre])
def get_genres(service: GenreService = Depends()):
    return service.get_list()


@router.get('/{id}', response_model=Genre)
def get_genre(genre_id: int, service: GenreService = Depends()):
    return service.get(genre_id)


@router.post('/', response_model=Genre)
def create_genre(
        genre_data: GenreCreate,
        service: GenreService = Depends()):
    return service.create(genre_data)
