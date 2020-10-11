from typing import Iterable, Optional

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    name: str = Field(..., env='APPLICATION_NAME')
    sources: Optional[Iterable[str]] = Field(None)

    class Config:
        env_file = '.env'


settings = Settings(
    sources=(
        'https://viruswaarheid.nl/feed/',
        'https://maurice.nl/feed/',
        'https://blog.cleancoder.com/atom.xml',
        'https://simpleprogrammer.com/feed/',
        'https://www.bitsoffreedom.nl/feed/',
        'https://www.xkcd.com/rss.xml',
        'http://www.israeltoday.nl/Portals/2/news.xml',
        'https://logos.nl/feed/',
        'https://css-tricks.com/feed/',
        'https://reinout.vanrees.org/weblog/atom.xml',
        'https://cip.nl/rss',
        'https://www.ellaster.nl/feed/',
        'https://stichtingvaccinvrij.nl/feed/',
        'https://testdriven.io/feed.xml',
        'https://expertvagabond.com/feed/',
        'https://www.ikwilmobielwerken.nl/feed/',
    )
)
