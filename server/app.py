from fastapi import FastAPI

import api
from server.database import engine
from server.tables import Base

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(api.router)

