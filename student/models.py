from django.db import models
from django.contrib.auth.models import User
from django.core .validators import FileExtensionValidator
import os
# Create your models here.
class StudentProfile(models.Model):
    courses = [
        ('Python Fullstack Development', 'Python Fullstack Development'),
        ('Java Fullstack Development', 'Java Fullstack Development'),
        ('MERN Fullstack Development', 'MERN Fullstack Development'),
        ('Fullstack Testing', 'Fullstack Testing')
    ]

    def get_upload_path(self, filename):
        ext = filename.split('.')[-1]
        filename = f"{self.username.first_name}_{self.username.last_name}_resume.{ext}"
        return os.path.join("students_resumes", filename)     
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    pno = models.CharField(max_length=50)
    add = models.TextField()
    course = models.CharField(max_length=50, choices=courses, default='Python Fullstack Development', null=True, blank=True)
    profile_pic = models.ImageField(upload_to='students_profiles/', null=True, blank=True)
    resume = models.FileField(upload_to=get_upload_path, validators=[FileExtensionValidator(['pdf', 'docx'])])

    def __str__(self):
        return self.username.username