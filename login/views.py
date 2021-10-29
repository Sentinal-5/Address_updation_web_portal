from django.shortcuts import render
from .forms import LoginForm
# Create your views here.


def home_view(request):
    context = {}
    context['form.as_table'] = LoginForm()
    return render(request, "login_page.html", context)