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
                for article in self.entries_to_articles(result.get('entries', []))[0:3]:
                    article.site_name = feed.title
                    article.site_url = feed.url
                    articles.append(article)
            except URLError as e:
                pass
        return articles, feeds

    def entries_to_articles(self, entries):
        result = list()
        for entry in entries:
            entry.update({
                'published': self.get_published_date(entry, 'published', 'updated', 'created'),
            })
            result.append(FeedParserArticle(**entry))
        return sorted(result, key=lambda x: x.published, reverse=True)

    def get_published_date(self, entry, *args):
        for value in [entry.get(key) for key in args]:
            if isinstance(value, str):
                return parser.parse(value)
        return datetime.now()