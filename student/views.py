from django.shortcuts import render
from student.forms import *
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def student_home(request):
    return render(request, 'student/student_home.html')


def student_register(request):
    ESUFO = StudentUserForm()
    ESPFO = StudentProfileForm()
    d = {'ESUFO': ESUFO, 'ESPFO': ESPFO}
    if request.method == 'POST' and request.FILES:
        SUFDO = StudentUserForm(request.POST)
        SPFDO = StudentProfileForm(request.POST, request.FILES)
        if SUFDO.is_valid() and SPFDO.is_valid():
            pw = SUFDO.cleaned_data.get('password')
            MSUFDO = SUFDO.save(commit=False)
            MSUFDO.set_password(pw)
            MSUFDO.save()
            MSPFDO = SPFDO.save(commit=False)
            MSPFDO.username = MSUFDO
            MSPFDO.save()
            return HttpResponse('Done....')
        return HttpResponse('Invalid Data')
    return render(request, 'student/student_register.html', d)