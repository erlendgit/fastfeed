from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class FeedParserArticle(BaseModel):
    title: str = Field(...)
    link: str = Field(...)
    published: datetime = Field(...)
    site_name: Optional[str] = Field(None)
    site_url: Optional[str] = Field(None)
