from typing import List

from fastapi import APIRouter, Depends

from server.models.movies import MovieCreate, Movie
from server.services.movies import MovieService

router = APIRouter(
    prefix='/movies',
)


@router.get('/', response_model=List[Movie])
def get_movies(service: MovieService = Depends()):
    return service.get_list()


@router.post('/', response_model=Movie)
def create_movie(
        movie_data: MovieCreate,
        service: MovieService = Depends()):
    return service.create(movie_data)


@router.get('/{id}', response_model=Movie)
def get_movie(movie_id: int, service: MovieService = Depends()):
    return service.get(movie_id)
