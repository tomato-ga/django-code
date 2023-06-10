from django.urls import path
from .views import FetchRSS, FeedList

urlpatterns = [
    path('fetch-rss/', FetchRSS.as_view(), name='fetch-rss'),
    path('', FeedList.as_view(), name='feed-list'),  # 追加
]
