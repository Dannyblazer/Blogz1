from django.urls import path
from .views import news_articles
app_name = "personal"

urlpatterns = [
    path('', news_articles, name="new_articles"),
]

