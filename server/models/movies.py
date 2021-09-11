from pydantic import BaseModel


class MovieBase(BaseModel):
    name: str
    country: str
    description: str
    year: int


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    pass
