from django.core.management import call_command
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from .models import Feed

class FetchRSS(View):
    def get(self, request, *args, **kwargs):
        call_command('fetch_rss')
        return HttpResponse('RSS feed fetched successfully')

class FeedList(ListView):
    model = Feed
    template_name = 'rss_feed/feed_list.html'  # 使用するテンプレート