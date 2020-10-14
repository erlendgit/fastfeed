from datetime import datetime
from typing import Iterable
from urllib.error import URLError

import feedparser
from dateutil import parser

from app.TempStore import TempStore
from app.models.FeedParserArticle import FeedParserArticle
from app.models.FeedParserResource import FeedParserResource


class Fetch(object):

    def __init__(self, sources: Iterable[str]):
        self.sources = sources

    @TempStore('fetch_feed_articles')
    def get_articles(self):
        feeds = []
        articles = []
        for source in self.sources:
            try:
                print("Parse %s" % source)
                result = feedparser.parse(source)
                feed = FeedParserResource(
                    feed_url=source,
                    url=result['feed']['link'],
                    title=result['feed']['title'])
                feeds.append(feed)
                for entry in result.get('entries')[0:3]:
                    entry.update({
                        'published': self.get_published_date(entry, 'published', 'updated', 'created'),
                    })
                    articles.append(FeedParserArticle(
                        **entry,
                        site_name=feed.title,
                        site_url=feed.url,
                    ))
            except URLError as e:
                pass
        return articles, feeds

    def get_published_date(self, entry, *args):
        for value in [entry.get(key) for key in args]:
            if isinstance(value, str):
                return parser.parse(value)
        return datetime.now()