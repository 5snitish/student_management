from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from users.serializers import  *
class StudentRegistrationView(RegisterView):
    serializer_class = StudentCustomRegistrationSerializer


class TeacherRegistrationView(RegisterView):
    serializer_class = TeacherCustomRegistrationSerializer



 