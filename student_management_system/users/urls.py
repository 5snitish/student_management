from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    #Registration Urls
    path('registration/student/', StudentRegistrationView.as_view(), name='register-seller'),
    path('registration/teacher/', TeacherRegistrationView.as_view(), name='register-buyer'),
    
]