from django.db import models
from datetime import datetime
from decouple import config
import praw #Reddit python library

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
        reddit = praw.Reddit(client_id = config('REDDIT_CLIENT_ID'),
            client_secret = config('REDDIT_SECRET'),
            user_agent = config('REDDIT_USER_AGENT'),
            username = config('REDDIT_USERNAME'),
            password = config('REDDIT_PASSWORD'))
        subreddit = reddit.subreddit('news') #r/news/
        hot_news = subreddit.hot(limit = 25)

        news_list = []
        for post in hot_news:
            news_list.append({'headline':post.title, 'link': post.url, 'source':'reddit', 'date': post.created})

        return news_list

    class Meta:
        proxy = True

class NewsAPI(NewsSource):
    objects = NewsAPIManager()

    def fetch_news(self):
        print('Fetch NewsAPI news')

    class Meta:
        proxy = True
