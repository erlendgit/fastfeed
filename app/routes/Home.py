import logging

from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from app.Fetch import Fetch
from app.templates import render
from settings import settings

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get('/', response_class=HTMLResponse)
async def home_page(request: Request):
    articles, feeds = Fetch(settings.sources).get_articles()
    return render('pages/home.html', {
        'request': request,
        'articles': sorted(articles, key=lambda x: x.published, reverse=True),
        'feeds': sorted(feeds, key=lambda x: x.title)
    })
