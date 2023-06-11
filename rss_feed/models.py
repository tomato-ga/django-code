from django.db import models


class FeedSource(models.Model):
    url = models.URLField()

    def __str__(self) -> str:
        return self.url


class Feed(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    source = models.ForeignKey(FeedSource, on_delete=models.CASCADE, related_name='feeds')

    def __str__(self):
        return self.title
