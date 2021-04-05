from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from users.serializers import  *
from .permission import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404



 # student registration view
class StudentRegistrationView(RegisterView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,is_super_admin,) or  (IsAuthenticated,is_Teacher,)

    serializer_class = StudentCustomRegistrationSerializer
   
# teacher registration view     
class TeacherRegistrationView(RegisterView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,is_super_admin,)

    serializer_class = TeacherCustomRegistrationSerializer

# to view student list    
class StudentViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,is_super_admin, ) or  (IsAuthenticated,is_Teacher,)
    def list(self,request):
        student = Student.objects.all()
        serializer = StudentDataSerializer(student, many= True, context = {"request":request})
        responce_dict = {"error":False,"message":"All Student List Data","data":serializer.data}
        return Response(responce_dict) 


 # to view teachers list
class TeacherViewSet(viewsets.ViewSet):
     permission_classes = (IsAuthenticated,is_super_admin,)
     def list(self,request):
        teacher = Teacher.objects.all() 
        serializer = TeacherDataSerializer(teacher, many= True, context = {"request":request})
        responce_dict = {"error":False,"message":"All Teacher List Data","data":serializer.data}
        return Response(responce_dict)    

#to get student data
class StudentData(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self,request):
        queryset = Student.objects.all()
         
        student = get_object_or_404 (queryset,student_id=request.user)
        
        serializer = StudentDataSerializer(student,context = {"request":request})
        dist_responce = {"error":False,"message":"Student deta fetched", "data":serializer.data}
        return Response(dist_responce )


