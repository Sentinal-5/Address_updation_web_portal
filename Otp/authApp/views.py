import re
from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,UserProfileForm
from .models import Profile
import requests
from django.contrib.auth.hashers import make_password
import random
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
# Create your views here.


def send_otp(number,message):
    url = "https://www.fast2sms.com/dev/bulk"
    api = "mEgndjuoSzp0c5lOwfyZJIFQKMxGDh2XNR39UH6kTs1Y4B8qv7A6uEpcJvTzaUw0oxYKZdmejgyNVrMk"
    querystring = {"authorization":api,"sender_id":"FSTSMS","message":message,"language":"english","route":"p","numbers":number}
    headers = {
        'cache-control': "no-cache"
    }
    return requests.request("GET", url, headers=headers, params=querystring)

    








def userLogin(request):

    try :
        if request.session.get('failed') > 2:
            return HttpResponse('<h1> You have to wait for 5 minutes to login again</h1>')
    except:
        request.session['failed'] = 0
        request.session.set_expiry(100)



    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            request.session['username'] = username
            request.session['password'] = password
            u = User.objects.get(username=username)
            p = Profile.objects.get(user=u)
            p_number = p.phone_number
            otp = random.randint(1000,9999)
            request.session['login_otp'] = otp
            aadhn = username[-4:]
            message = f'Your OTP for Aadhar Noumber - XXXXXXXX{aadhn} is {otp}'
            send_otp(p_number,message)
            return redirect('/login/otp/')
        else:
            messages.error(request,'username or password is wrong')
    return render(request,'login.html')

def otpLogin(request):
    if request.method == "POST":
        username = request.session['username']
        password = request.session['password']
        otp = request.session.get('login_otp')
        u_otp = request.POST['otp']
        if int(u_otp) == otp:
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                request.session.delete('login_otp')
                messages.success(request,'login successfully')
                return redirect('/')
        else:
            messages.error(request,'Wrong OTP')
    return render(request,'login-otp.html')

def home(request):


    return render(request,'home.html')




