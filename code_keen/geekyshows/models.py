from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=10)
    img=models.ImageField(upload_to='images')
