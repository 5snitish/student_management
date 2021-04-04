from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_student = models.BooleanField(default=False)
  is_teacher = models.BooleanField(default=False)
  is_super_admin = models.BooleanField(default=False) 
class Student(models.Model):
    student = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    rollno = models.CharField(max_length=100)
    standerd  = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=12)

    def __str__(self):
        return self.student.username

class Teacher(models.Model):
    teacher = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    designation= models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=12) 
    def __str__(self):
        return self.teacher.username