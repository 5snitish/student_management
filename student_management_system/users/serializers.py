from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from users.models import *

class StudentCustomRegistrationSerializer(RegisterSerializer):
    student = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    rollno = serializers. CharField(required=True )
    standerd  = serializers. CharField( required=True)
    fathername = serializers.CharField(required=True )
    mothername = serializers. CharField( required=True)
    phoneno = serializers. CharField(required=True )
    
    def get_cleaned_data(self):
            data = super(StudentCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'rollno':  self.validated_data.get("rollno",'' ),
                'standerd':  self.validated_data.get('satnderd','' ),
                'fathername':  self.validated_data.get('fathername',''),
                'mothername':  self.validated_data.get('mothername',''),
                'phoneno':  self.validated_data.get('phoneno' ),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(StudentCustomRegistrationSerializer, self).save(request)
        user.is_student = True
        user.save()
        student = Student(student=user,rollno=self.get_cleaned_data("rollno"),
                standerd= self.get_cleaned_data('satnderd'),
                fathername=   self.get_cleaned_data('fathername'),
                mothername=   self.get_cleaned_data('mothername'),
                phoneno=   self.get_cleaned_data('phoneno' ))
        student.save()
        return user 


class TeacherCustomRegistrationSerializer(RegisterSerializer):
    Teacher = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
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
        user.save()
        teacher = Teacher(buyer=user, 
                designation=  self.get_cleaned_data('designation' ),
                fathername=   self.get_cleaned_data('fathername' ),
                mothername=   self.get_cleaned_data( 'mothername' ),
                phoneno=   self.get_cleaned_data('phoneno' ))
        teacher.save()
        return user




