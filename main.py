import locale

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.routes import Home, ClearCache

app = FastAPI(docs_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")

locale.setlocale(locale.LC_TIME, 'nl_NL')


app.include_router(Home.router)
app.include_router(ClearCache.router)

# Allow debugging!
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
