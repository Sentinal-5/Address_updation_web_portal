from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
# Create your views here.


# Create your views here.
def home_view(request):
    context = {}
    context['form.as_table'] = LoginForm()
    return render(request, "login_page.html", context)

"""
def login(request):

    if request.method == 'POST':
        inp = request.POST.get('user_input')
"""
