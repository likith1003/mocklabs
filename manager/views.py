from django.shortcuts import render
from manager.forms import *
from django.http import HttpResponse, HttpResponseRedirect
import random
import string
from django.urls import reverse

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