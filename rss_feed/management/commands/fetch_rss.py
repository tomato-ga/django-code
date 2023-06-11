# apps/rss_feed/management/commands/fetch_rss.py

import feedparser
from django.core.management.base import BaseCommand

from rss_feed.models import Feed, FeedSource

class Command(BaseCommand):
    help = 'Fetches RSS feed and stores in database'

    def handle(self, *args, **kwargs):
        rss_urls = ['https://rss.itmedia.co.jp/rss/2.0/itmedia_all.xml', 'https://b.hatena.ne.jp/hotentry/it.rss']

        for rss_url in rss_urls:
            feed_source, created = FeedSource.objects.get_or_create(url=rss_url)
            feed = feedparser.parse(rss_url)

            for entry in feed.entries:
                Feed.objects.get_or_create(
                    title=entry.title,
                    link=entry.link,
                    source=feed_source,
                )
