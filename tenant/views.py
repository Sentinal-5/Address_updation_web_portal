from django.shortcuts import render
from .forms import TenantForm
# Create your views here.

def tenant_view(request):
    if request.method =='POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            pass
        else:
            pass


