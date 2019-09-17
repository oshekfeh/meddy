# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from newsaggregator.serializers import NewsSerializer
from newsaggregator.utilites import NewsCollector

@api_view(['GET'])
def news_list(request):
    query = request.GET.get('query')
    news = NewsCollector().fetch_news(query)
    results = NewsSerializer(news, many=True).data
    return Response(results)
