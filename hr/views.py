from django.shortcuts import render
from manager.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from hr.forms import *
import csv
from django.core.mail import send_mail

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

def schedule_mock(request):
    un = request.session.get('hruser')
    if un:
        UO = User.objects.get(username=un)
        PO = EmployeeProfile.objects.get(username = UO)
    ESFO = SchedulingForm()
    d = {'ESFO': ESFO}
    if request.method == 'POST' and request.FILES:
        SFDO = SchedulingForm(request.POST, request.FILES)
        if SFDO.is_valid():
            SFDO.save()
            with open(r"C:\Users\lenovo\Desktop\Book1.csv", 'r') as f:
                data = csv.reader(f)
                next(data)
                usernames = [i[1]+i[2] for i in data]
                for un in usernames:
                    SO = User.objects.get(username=un)
                    if SO:
                        message=f''' Dear {{un}},

I hope you’re doing well! We are excited to invite you for a mock interview as part of your preparation for the  at Qspiders Bhubaneswar. This session is designed to help you practice and receive constructive feedback before your official interview.

Interview Details:
📅 Date: {SFDO.cleaned_data.get('date')}
⏰ Time: {SFDO.cleaned_data.get('time')}
📍 Location/Platform: QSpiders Bhubaneswar
⏳ Duration: 30min

During the mock interview, we will focus on {SFDO.cleaned_data.get('subject')}, followed by a feedback session.

Please confirm your availability at your earliest convenience. Feel free to reach out if you have any questions. We look forward to helping you prepare!

Best regards,
{UO.first_name}
{PO.role}
Qspiders BBSR
{PO.pno}
'''
                        send_mail(
                            'RE: Invitation for Mock Interview – QSpiders Bhubaneswar',
                            message,
                            'likith.qsp@gmail.com',
                            ['likith.qsp@gmail.com'],
                            fail_silently=False


                        )

            return HttpResponseRedirect(reverse('hr_home'))
        return HttpResponse('invalid data')
    return render(request, 'hr/schedule_mock.html', d)