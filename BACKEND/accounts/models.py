from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.db import models
from django.conf import settings

class User(AbstractUser):
    pass

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_pk': user.pk,
        })

class Student(models.Model):
    s_num=models.CharField(max_length=10) #학번
    img=models.CharField(max_length=500,null=True,blank=True,default='') #이미지경로
    class_num=models.IntegerField() #반
    name=models.CharField(max_length=500) #이름
    y_num=models.IntegerField() #기수
    region=models.CharField(max_length=500) #지역

    


    