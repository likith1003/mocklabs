from django.urls import path
from manager.views import *

urlpatterns = [
    path('manager_home', manager_home, name='manager_home'),
    path('add_employee', add_employee, name='add_employee')
]
