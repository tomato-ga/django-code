from django.db import models

class Feed(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    # 必要に応じて他のフィールドも追加

    def __str__(self):
        return self.title
