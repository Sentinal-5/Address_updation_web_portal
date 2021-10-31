from django.shortcuts import render
from .forms import LandlordForm
from django.contrib import messages
from login.models import Users,activeuser

# Create your views here.
def landlord_view(request):
    if request.method == 'POST':
        form = LandlordForm(request.POST)
        if form.is_valid():
            # verify otp
            if form.cleaned_data("otp")==activeuser.objects.all()[:1].get():
                pass
            #change add
            pass

        else:
            messages.error(request, 'SOMETHING WENT WRONG!')
