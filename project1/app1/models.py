from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class employer_registration(models.Model):
    username=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    image=models.ImageField(upload_to='employer')
    password=models.CharField(max_length=200)

    def __str__(self): 
        return self.username
    
class employee_registration(models.Model):
    workername=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    occupation=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    image=models.ImageField(upload_to='employer')
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.workername + '-(' + self.occupation +')'
    
class job(models.Model):
    username=models.ForeignKey(employer_registration, on_delete=models.CASCADE)
    workername=models.ForeignKey( employee_registration, on_delete=models.CASCADE)
    job_description=models.TextField()
    job_location=models.CharField(max_length=200)
    job_date=models.DateField(max_length=200)
    job_review=models.CharField(max_length=200)

    # def __str__(self):
    #     return self.workername+return self.workername

class acknowledgement(models.Model):
    username=models.ForeignKey(employer_registration, on_delete=models.CASCADE)
    workername=models.ForeignKey(employee_registration, on_delete=models.CASCADE)
    wphone=models.CharField(max_length=200)
    ackmesg=models.TextField()
  