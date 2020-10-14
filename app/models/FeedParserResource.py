from pydantic import BaseModel, Field


class FeedParserResource(BaseModel):
    title: str = Field(...)
    url: str = Field(...)
    feed_url: str = Field(...)
