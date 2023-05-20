from django.urls import path
from .views import news_articles
urlpatterns = [
    path('', news_articles, name="new_articles"),
]
