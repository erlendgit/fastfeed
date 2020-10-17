from typing import Optional

from fastapi import APIRouter
from fastapi.params import Query

from app.Fetch import Fetch
from app.TempStore import TempStore
from settings import settings

router = APIRouter()


@router.get('/clearcache')
async def clearcache_page(key: Optional[str] = Query(None)):
    if key is None or settings.clearcache != key:
        return {"msg": "not ok"}
    TempStore.clear_all()
    Fetch(settings.sources).get_articles()
    return {"msg": "ok"}
