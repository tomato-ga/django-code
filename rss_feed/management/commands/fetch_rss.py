# apps/rss_feed/management/commands/fetch_rss.py

import feedparser
from django.core.management.base import BaseCommand

from rss_feed.models import Feed

class Command(BaseCommand):
    help = 'Fetches RSS feed and stores in database'

    def handle(self, *args, **kwargs):
        feed = feedparser.parse('https://rss.itmedia.co.jp/rss/2.0/itmedia_all.xml')

        for entry in feed.entries:
            # データをデータベースに保存するロジックをここに書く
            Feed.objects.get_or_create(
                title=entry.title,
                link=entry.link,
                # 他のフィールドも適宜追加
            )
