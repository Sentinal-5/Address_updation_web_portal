from random import random
from django.shortcuts import render,redirect
from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render
from .forms import TenantForm
from .forms import TenantForm
from django.contrib import messages


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


def tenant_view(request):
    try:
        if request.session.get('failed') > 2:
            return HttpResponse('<h1> You have to wait for 5 minutes to login again</h1>')
    except:
        request.session['failed'] = 0
        request.session.set_expiry(100)

    if request.method == 'POST':
        form = TenantForm(request.POST or None)
        if form.is_valid():
            landlord_num = form.cleaned_data.get("landlord_number")
            address = form.cleaned_data.get("address")
        else:
            messages.error(request, 'SOMETHING WENT WRONG!')

        otp = random.randint(1000, 9999)
        request.session['login_otp'] = otp
        pn = landlord_num[-4:]
        message = f'Your OTP for address access - XXXXXXXX{pn} is {otp}'
        send_otp(landlord_num, message)


        return redirect('login/tenant/confirmation')

def confirm_view(request):
    return HttpResponse("DONE!")


