from datetime import datetime
from django.utils import timezone
#from time import timezone
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
import datetime

# Create your models here.

'''
types = [('Msc.Information Technology','Msc.Information Technology'),('Chemistry','Chemistry')]
class Users(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date = models.DateField(null=True)
    phone = models.BigIntegerField()
    email = models.EmailField(null=True)
    degree = models.CharField(choices=types,max_length=100,null=True,blank=False)
    image = models.ImageField(upload_to ='media/')
    def __str__(self):
        return self.degree
'''
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100,null=True)
    middle_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    date = models.DateField(null=True)
    phone = models.BigIntegerField(null=True)
    email = models.EmailField(null=True)
    type=models.CharField(max_length=100,null=True)
    degree=models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to ='images',blank=True)
    password=models.CharField(max_length=100,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.first_name

class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name=models.CharField(max_length=100)
    def __str__(self):
        return self.class_name
class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.subject_name
class Lecture(models.Model):
    classid=models.IntegerField(null=True)
    subjectid=models.IntegerField(null=True)
    teacher_id=models.IntegerField(null=True)
    #today = datetime.datetime.now()
    #date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
    date =models.DateField()
    #time=models.DateTimeField(auto_now_add=True,blank=True)
    #time=models.TimeField()
    def __str__(self):
        return self.classid
class Presenty(models.Model):
    id=models.AutoField(primary_key=True)
    lectu_id=models.IntegerField(null=True)
    stud_id=models.IntegerField(null=True)
    presenty=models.CharField(max_length=100,default=False)
    def __str__(self):
        return self.id