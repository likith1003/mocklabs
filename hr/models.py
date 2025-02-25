from django.db import models
from django.core.validators import FileExtensionValidator
import os
from django.contrib.auth.models import User
subjects = [
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('Django', 'Django'),
        ('Spring', 'Spring'),
        ('Hibernet', 'Hibernet'),
        ('SQL', 'SQL'),
        ('Web-Technology', 'Web-Technology'),
        ('React JS', 'React JS'),
        ('MongoDB', 'MongoDB'),
        ('Express JS', 'Express JS')
    ]
# Create your models here.
class Schedulings(models.Model):
    def get_upload_path(self, filename):
        ext = filename.split('.')[-1]
        filename = f"Slot_{self.trainer.username}.{ext}"
        return os.path.join("Slots", filename)
    

    slot_id = models.IntegerField(primary_key=True)
    students = models.FileField(upload_to=get_upload_path, max_length=100, validators=[FileExtensionValidator(['csv'])])
    subject = models.CharField(max_length=50, choices=subjects)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='slots')
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.trainer.username}_{self.slot_id}"
    