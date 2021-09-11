from pydantic import BaseModel


class BaseGenre(BaseModel):
    title: str
    color: str


class Genre(BaseGenre):
    id: int

    class Config:
        orm_mode = True


class GenreCreate(BaseGenre):
    pass


class GenreUpdate(BaseGenre):
    pass
