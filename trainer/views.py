from django.shortcuts import render
from manager.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.



def trainer_home(request):
    return render(request, 'trainer/trainer_home.html')

def trainer_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un, password=pw)
        if AUO and AUO.is_staff and AUO.is_active:
            PO = EmployeeProfile.objects.get(username=AUO)
            if PO.role == 'Trainer':
                login(request, AUO)
                request.session['hruser']=un
                return HttpResponseRedirect(reverse('trainer_home'))
            return HttpResponse('not a Trainer')
        return HttpResponse('Invalid Credentials')
    return render(request, 'trainer/trainer_login.html')


def trainer_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('trainer_home'))