from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from users.models import *


# to save the student data  
class StudentCustomRegistrationSerializer(RegisterSerializer):
    student = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    first_name = serializers.CharField(required=True )
    last_name = serializers.CharField(required=True )

    rollno = serializers. CharField(required=True )
    standerd  = serializers. CharField( required=True)
    fathername = serializers.CharField(required=True )
    mothername = serializers. CharField( required=True)
    phoneno = serializers. CharField(required=True )
    
    def get_cleaned_data(self):
            data = super(StudentCustomRegistrationSerializer, self).get_cleaned_data()
            
            extra_data = {
                'rollno':  self.validated_data.get("rollno",'' ),
                'standerd':  self.validated_data.get('standerd','' ),
                'fathername':  self.validated_data.get('fathername',''),
                'mothername':  self.validated_data.get('mothername',''),
                'phoneno':  self.validated_data.get('phoneno','' ),
            }
            data.update(extra_data)
            print(data)
            return data

    def save(self, request):
         
        user = super(StudentCustomRegistrationSerializer, self).save(request)
        user.is_student = True 
        user.groups_id= 3
        user.save()
        student = Student(student=user,
                rollno=self.cleaned_data.get('rollno'),
                standerd= self.cleaned_data.get('standerd'),
                fathername=   self.cleaned_data.get('fathername'),
                mothername=   self.cleaned_data.get('mothername'),
                phoneno=   self.cleaned_data.get('phoneno' ))
        student.save()
        return user 

# to save the teachers data
class TeacherCustomRegistrationSerializer(RegisterSerializer):
    Teacher = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    first_name = serializers.CharField(required=True )
    last_name = serializers.CharField(required=True )
    designation= serializers.CharField(required=True )
    fathername = serializers.CharField(required=True )
    mothername = serializers.CharField(required=True )
    phoneno = serializers.CharField(required=True )
    
    
    def get_cleaned_data(self):
            data = super(TeacherCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'designation':self.validated_data.get("designation",''), 
                'fathername':  self.validated_data.get('fathername',''),
                'mothername':  self.validated_data.get('mothername',''),
                'phoneno':  self.validated_data.get('phoneno' ),
                }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(TeacherCustomRegistrationSerializer, self).save(request)
        user.is_Teacher = True
        user.groups = 2
        user.save()
        teacher = Teacher(buyer=user, 
                designation=  self.cleaned_data.get('designation' ),
                fathername=   self.cleaned_data.get('fathername' ),
                mothername=   self.cleaned_data.get( 'mothername' ),
                phoneno=   self.cleaned_data.get('phoneno' ))
        teacher.save()
        return user


# to retrive the user data with list of student or teacher

class UserSerializer(serializers.ModelSerializer):
        class Meta:
                model=User
                fields = ("username","email","first_name","last_name")    


# to retrive the list to students
class StudentDataSerializer(serializers.ModelSerializer):
        class Meta:
                model = Student
                fields = "__all__"

        def to_representation(self, instance ) :
                responce = super().to_representation(instance)
                responce ['student'] = UserSerializer(instance.student).data
                return responce        


# to retrive the teachers list
class TeacherDataSerializer(serializers.ModelSerializer):
        class Meta:
                model = Teacher
                fields = "__all__"
        def to_representation(self, instance ) :
                responce = super().to_representation(instance)
                responce ['teacher'] = UserSerializer(instance.teacher).data
                return responce