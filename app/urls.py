from django.urls import path
from . import views
# from .views import BlogsList, BlogPostView

app_name = "app"

urlpatterns = [
    path('', views.home, name="home"),
    path('blogs', views.blogs, name="blogs"),
    # path('blogs', BlogsList.as_view(), name="blogs"),
    path('article/<int:pk>', views.blog_article, name="article"),
    # path('article/<int:pk>', BlogPostView.as_view(), name="article"),
    path('post-blog', views.blog_register, name="post-blog"),
    path('post', views.make_a_post, name="post"),
]


