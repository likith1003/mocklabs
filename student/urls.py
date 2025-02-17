from django.urls import path
from student.views import *

urlpatterns = [
    path('student_home', student_home, name='student_home'),
    path('student_register', student_register, name='student_register')   
]
