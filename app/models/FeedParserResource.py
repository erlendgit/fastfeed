from pydantic import BaseModel, Field


class FeedParserResource(BaseModel):
    title: str = Field(...)
    link: str = Field(...)
    feed_url: str = Field(...)
