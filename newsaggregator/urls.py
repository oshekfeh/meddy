from django.urls import path

from . import views

app_name = 'newsaggregator'

urlpatterns = [
    path('news/', views.news_list, name='list'),
]
