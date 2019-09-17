# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from newsaggregator.serializers import NewsSerializer

# Create your views here.
@api_view(['GET'])
def news_list(request):
    news = [{'headline':'first title', 'link':'first link', 'source':'reddit'},
            {'headline':'second title', 'link':'second link', 'source':'newsapi'}]
    results = NewsSerializer(news, many=True).data
    return Response(results)
