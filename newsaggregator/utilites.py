from newsaggregator.models import NewsSource, Reddit, NewsAPI

class NewsCollector():
    def __init__(self):
        print("Collector initiated")

    def fetch_news(self, query=None):
        SOURCE_TYPE_TO_CLASS_MAP = {
            'reddit':'Reddit',
            'newsapi':'NewsAPI'
        }
        sources = NewsSource.objects.all()
        news = []
        for source in sources:
            class_name = SOURCE_TYPE_TO_CLASS_MAP[source.source_name]
            source_news = globals()[class_name](source).fetch_news(query)
            news.extend(source_news)

        #sort news by date from old to new
        from operator import itemgetter
        return sorted(news, key=itemgetter('date'), reverse=True)
