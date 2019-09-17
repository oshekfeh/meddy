from django.db import models
from datetime import datetime

# Create your models here.

SOURCES_NAMES = (
    ('reddit', 'Reddit'),
    ('newsapi', 'NewsAPI')
)

#News sources class, subclasses and managers
class RedditManager(models.Manager):
    def get_queryset(self):
        return super(RedditManager, self).get_queryset().filter(
            source_name='reddit')

class NewsAPIManager(models.Manager):
    def get_queryset(self):
        return super(NewsAPIManager, self).get_queryset().filter(
            source_name='newsapi')

class NewsSource(models.Model):
    source_name = models.CharField(max_length=200, choices=SOURCES_NAMES, unique=True)


class Reddit(NewsSource):
    objects = RedditManager()

    def fetch_news(self):
        print('Fetch reddit news')

    class Meta:
        proxy = True

class NewsAPI(NewsSource):
    objects = NewsAPIManager()

    def fetch_news(self):
        print('Fetch NewsAPI news')

    class Meta:
        proxy = True
