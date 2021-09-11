from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from .. import tables
from ..database import get_session
from ..models.genres import GenreCreate


class GenreService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, genre_id: int) -> tables.Genre:
        genre = self.session.get(tables.Genre, genre_id)
        if not genre:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return genre

    def create(self, genre_data: GenreCreate) -> tables.Genre:
        genre = tables.Genre(**genre_data.dict())
        self.session.add(genre)
        self.session.commit()
        return genre

    def get_list(self) -> List[tables.Genre]:
        return self.session.query(tables.Genre).all()

    def get(self, genre_id: int) -> tables.Genre:
        return self._get(genre_id)
