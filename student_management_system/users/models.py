from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from django.conf import settings

# fro sending email for password reset
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

# to create user
class User(AbstractUser):
  #Boolean fields to select the type of account.
  firs_tname = models.CharField(max_length=50)
  last_name = models.CharField(max_length= 100)
  is_student = models.BooleanField(default=False)
  is_teacher = models.BooleanField(default=False)
  is_super_admin = models.BooleanField(default=False)
  groups = models.ForeignKey(Group, on_delete=models.CASCADE, default = 1) 


 # to create user with student details 
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

# to create user with teacher details 
class Teacher(models.Model):
    teacher = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    designation= models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=12) 
    def __str__(self):
        return self.teacher.username

# to send email for reset password

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="student management system"),
        # message:
        email_plaintext_message,
        # from:
        "snitish515@gmail.com",
        # to:
        [reset_password_token.user.email]
    )
