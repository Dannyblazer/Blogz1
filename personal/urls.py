<<<<<<< HEAD
from django.urls import path
from .views import news_articles
app_name = "personal"

urlpatterns = [
    path('', news_articles, name="new_articles"),
]
=======
from django.urls import path
from .views import news_articles
urlpatterns = [
    path('', news_articles, name="new_articles"),
]
>>>>>>> f8e9cabd2a6e26705433f3807b1e00e632b64474
