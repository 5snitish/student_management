from django.urls import path,include
from users.views import *

from rest_framework import routers
app_name = 'users'


router = routers.DefaultRouter()
# to view the list of the students
router.register("student",StudentViewSet, basename="Student")
# to view the list of teachers 
router.register("teacher",TeacherViewSet, basename="Teacher")
# to view the data of students
router.register("studentdata",StudentData, basename = "studentData")
urlpatterns = [
    # list urls
    path('list/', include(router.urls)),

    #Registration Urls
    # use api/ before these
    path('registration/student/', StudentRegistrationView.as_view(), name='register-seller'),
    path('registration/teacher/', TeacherRegistrationView.as_view(), name='register-buyer'),
    
]