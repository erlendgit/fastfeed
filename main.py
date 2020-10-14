from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.routes import Home

app = FastAPI(docs_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(Home.router)

# Allow debugging!
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
