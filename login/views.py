from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Users, activeuser
import random
from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from .forms import LoginForm


# Create your views here.

def send_otp(number, message):
    url = "https://www.fast2sms.com/dev/bulk"
    api = "mEgndjuoSzp0c5lOwfyZJIFQKMxGDh2XNR39UH6kTs1Y4B8qv7A6uEpcJvTzaUw0oxYKZdmejgyNVrMk"
    querystring = {"authorization": api, "sender_id": "FSTSMS", "message": message, "language": "english", "route": "p",
                   "numbers": number}
    headers = {
        'cache-control': "no-cache"
    }
    return requests.request("GET", url, headers=headers, params=querystring)


def userLogin(request):
    activeuser.objects.all().delete()
    try:
        if request.session.get('failed') > 2:
            return HttpResponse('<h1> You have to wait for 5 minutes to login again</h1>')
    except:
        request.session['failed'] = 0
        request.session.set_expiry(100)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['username'] = username
            request.session['password'] = password
            u = User.objects.get(username=username)
            person = Users.objects.get(user=u)
            p_number = person.phone_number
            address = person.address
            activeuser.objects.create(user=person, phone_number=p_number, address=address)
            return redirect('/login/option/')
        else:
            messages.error(request, 'username or password is wrong')
    return render(request, 'login.html')


def option_view(request):
    if request.method == 'POST':
        if request.POST['option'] == 'tenant':
            return redirect('/login/tenant')
        if request.POST['option'] == 'landlord':
            return redirect('/login/landlord')
