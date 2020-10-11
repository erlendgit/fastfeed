from fastapi import FastAPI

from app.routes import Home

app = FastAPI(docs_url=None)
app.include_router(Home.router)
