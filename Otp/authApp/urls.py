from django.urls import path
from .import views
from django.contrib.auth import views as auth_view
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.userLogin, name="user-login"),
    path('login/otp/',views.otpLogin, name="otp-login"),
    path('logout/',auth_view.LogoutView.as_view(template_name='logout.html')),


    
]
