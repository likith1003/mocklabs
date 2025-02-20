from django.shortcuts import render
from manager.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def hr_home(request):
    return render(request, 'hr/hr_home.html')


def hr_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un, password=pw)
        if AUO and AUO.is_staff and AUO.is_active:
            PO = EmployeeProfile.objects.get(username=AUO)
            if PO.role == 'HR':
                login(request, AUO)
                request.session['hruser']=un
                return HttpResponseRedirect(reverse('hr_home'))
            return HttpResponse('not a HR')
        return HttpResponse('Invalid Credentials')
    return render(request, 'hr/hr_login.html')


def hr_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('hr_home'))