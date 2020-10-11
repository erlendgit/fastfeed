from fastapi import APIRouter

from app.Fetch import Fetch
from app.settings import settings

router = APIRouter()


@router.get('/')
async def home_page():
    articles, feeds = Fetch(settings.sources).get_articles()
    return sorted(articles, key=lambda a: a.sort_key(), reverse=True)
