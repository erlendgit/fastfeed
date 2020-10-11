from datetime import datetime
from typing import Optional

from dateutil import parser
from pydantic import BaseModel, Field, validator


class FeedParserArticle(BaseModel):
    title: str = Field(...)
    link: str = Field(...)
    published: Optional[datetime] = Field(None)
    created: Optional[datetime] = Field(None)
    updated: Optional[datetime] = Field(None)
    site_name: str = Field(...)
    site_url: str = Field(...)

    def sort_key(self):
        return self.published or self.created or self.updated

    @validator('published', 'created', 'updated', pre=True)
    def parse_published(cls, v):
        if isinstance(v, str):
            return parser.parse(v)
        return v
