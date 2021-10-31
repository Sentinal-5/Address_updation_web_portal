from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.userLogin, name="user-login"),
    path('login/option/', views.option_view, name="option"),

]