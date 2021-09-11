import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    country = sa.Column(sa.String)
    description = sa.Column(sa.Text)
    year = sa.Column(sa.Integer)


class Genre(Base):
    __tablename__ = 'genres'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String)
    color = sa.Column(sa.String)
