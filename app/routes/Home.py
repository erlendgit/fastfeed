from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from app.Fetch import Fetch
from app.templates import render
from settings import settings

router = APIRouter()


@router.get('/', response_class=HTMLResponse)
async def home_page(request: Request):
    articles, feeds = Fetch(settings.sources).get_articles()
    return render('pages/home.html', {
        'request': request,
        'articles': articles,
        'feeds': feeds
    })  # articles

# @router.get('/', response_class=HTMLResponse)
# async def home_page(request: Request):
#     articles, feeds = Fetch(settings.sources).get_articles()
#     return render('index.html', {
#         'request': request,
#         'articles': sorted(articles, key=lambda a: a.sort_key(), reverse=True)
#     })
