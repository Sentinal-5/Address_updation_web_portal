from django.urls import path
from .views import tenant_view, confirm_view
from django.contrib.auth import views as auth_view
from django.views.generic import TemplateView

urlpatterns = [
    path('login/tenant', tenant_view),
    path('login/tenant/confirmation', confirm_view),
]