from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    element=models.CharField( max_length=50)
    conselation=models.CharField(max_length=50)
    havetodo=models.CharField(max_length=50)
    completed=models.BooleanField(null=True,default=True)
    