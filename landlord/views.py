from django.shortcuts import render
from .forms import LandlordForm


# Create your views here.
def landlord_view(request):
    if request.method == 'POST':
        form = LandlordForm(request.POST)
        if form.is_valid():
            pass
        else:
            pass
