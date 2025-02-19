from django.shortcuts import render
from manager.forms import *
from django.http import HttpResponse, HttpResponseRedirect
import random
import string
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def manager_home(request):
    return render(request, 'manager/manager_home.html')

def add_employee(request):
    EEUFO = EmployeeUserForm()
    EEPFO = EmployeeProfileForm()
    d = {'EEUFO': EEUFO, 'EEPFO': EEPFO}
    if request.method == 'POST':
        EUFDO = EmployeeUserForm(request.POST)
        EPFDO = EmployeeProfileForm(request.POST)
        if EUFDO.is_valid() and EPFDO.is_valid():
            un = f"{EUFDO.cleaned_data.get('first_name')}{EPFDO.cleaned_data.get('pno')[-4:]}"
            pw = ''.join([random.choice(string.punctuation) for i in range(1, 6)])
            MEUFDO = EUFDO.save(commit=False)
            MEUFDO.username = un
            MEUFDO.set_password(pw)
            MEUFDO.is_staff=True
            MEUFDO.save()
            MEPFDO = EPFDO.save(commit=False)
            MEPFDO.username = MEUFDO
            MEPFDO.save()
            print(f"The username is {un}")
            print(f"The password is {pw}")
            return HttpResponseRedirect(reverse('manager_home'))
        return HttpResponse('Invalid Data')
    return render(request, 'manager/add_employee.html', d)


def manager_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un, password=pw)
        if AUO and AUO.is_staff and AUO.is_active:
            if AUO.is_superuser:
                login(request, AUO)
                request.session['adminuser']=un
                return HttpResponseRedirect(reverse('manager_home'))
            return HttpResponse('not a admin')
        return HttpResponse('byeeeee')
    return render(request, 'manager/manager_login.html')

def manager_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('manager_home'))