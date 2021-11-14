from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Student

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['pk','username']
 
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =['pk', 's_num','class_num','name','y_num','region']

class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =['pk','s_num','class_num','name','y_num','region']