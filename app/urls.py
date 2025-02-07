from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.home, name="home"),
    path('blogs', views.blogs, name="blogs"),
    path('article/<int:pk>', views.blog_article, name="article"),
    path('post-blog', views.blog_register, name="post-blog"),
    path('post', views.make_a_post, name="post"),
    path('profile', views.profile, name='profile'),
    path('edit_blog/<int:pk>', views.edit_blog, name='edit_blog'),
    path('login', views.user_login, name='login'),
    path('signin', views.signin, name='signin'),
]


