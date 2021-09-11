from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.movies import MovieCreate


class MovieService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, movie_id: int) -> tables.Movie:
        movie = self.session.get(tables.Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return movie

    def get_list(self) -> List[tables.Movie]:
        return self.session.query(tables.Movie).all()

    def create(self, movie_data: MovieCreate) -> tables.Movie:
        movie = tables.Movie(name=movie_data.name, country=movie_data.country,
                             description=movie_data.description,
                             year=movie_data.year)
        self.session.add(movie)
        self.session.commit()
        return movie

    def get(self, movie_id: int) -> tables.Movie:
        return self._get(movie_id)
