from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class FeedParserArticle(BaseModel):
    title: str = Field(...)
    link: str = Field(...)
    published: Optional[datetime] = Field(None)
    site_name: str = Field(...)
    site_url: str = Field(...)
