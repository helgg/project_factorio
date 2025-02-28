from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('home', views.logout_view, name='logout'),
    path('signup', views.user_register, name='signup'),

]

