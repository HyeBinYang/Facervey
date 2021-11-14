from django.db import models
from django.conf import settings
from accounts.models import Student

class Survey_Question(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    q_type=models.CharField(max_length=200) #질문유형 (객관식/단답식)
    content=models.CharField(max_length=500,null=True,blank=True,default='unknown') #질문내용

class Survey(models.Model):
    title=models.CharField(max_length=200,null=True,blank=True,default='untitled') #설문지 이름
    description=models.CharField(max_length=500,null=True,blank=True,default='') # 설문지 설명
    color=models.CharField(max_length=200,null=True,blank=True,default='#FFCDD2') #배경색
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) #설문지 처음생성시간
    updated_at = models.DateTimeField(auto_now=True)
    students=models.ManyToManyField(Student, related_name='surveys')
    questions=models.ManyToManyField(Survey_Question, related_name='surveyss')

class Multiple_Answer(models.Model):
    s_pk=models.ForeignKey(Survey,on_delete=models.CASCADE)
    q_pk=models.ForeignKey(Survey_Question,on_delete=models.CASCADE)
    content=models.CharField(max_length=500,null=True,blank=True,default='option') #선택지내용

class Student_Answer(models.Model):
    s_pk=models.ForeignKey(Survey,on_delete=models.CASCADE) #설문지번호
    st_pk=models.ForeignKey(Student,on_delete=models.CASCADE) #학생pk
    q_pk=models.ForeignKey(Survey_Question,on_delete=models.CASCADE) #질문번호
    answer=models.CharField(max_length=500,null=True, blank=True,default='') #학생의 답
    # s_num=models.ForeignKey(Student,on_delete=models.CASCADE) # 학번
