<<<<<<< HEAD
from django.urls import path
=======
from django.urls import path, include
>>>>>>> f8e9cabd2a6e26705433f3807b1e00e632b64474
from blog.views import create_blog_view, detail_blog_view, edit_blog_view, blog_like, create_comment, delete_comment

app_name = 'blog'

urlpatterns = [
    path('create/', create_blog_view, name="create"),
    path('<slug>/', detail_blog_view, name="detail"),
    path('<blog_id>/create_com/', create_comment, name="create_comment"),
    path('<com_id>/delete_com', delete_comment, name="delete_comment"),
    path('<slug>/edit', edit_blog_view, name="edit"),
    path('like/<pk>', blog_like, name="like"),
]
