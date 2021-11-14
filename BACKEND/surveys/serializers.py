from rest_framework import serializers
from .models import Survey, Survey_Question, Student_Answer, Multiple_Answer
from accounts.serializers import UserSerializer, StudentSerializer
from accounts.models import Student

class MAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Multiple_Answer
        fields=['pk','s_pk','q_pk','content']

class MAnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Multiple_Answer
        fields=['pk', 'q_pk','content']


class QuestionSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Survey_Question
        fields =['pk','user','content','q_type','surveyss']

class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey_Question
        fields =['pk','content','q_type']

class SurveySerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Survey
        fields =['pk','color','title','description','user',]
 
class SurveyListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Survey
        fields =['pk', 'created_at','color','title','description','user']

class StudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Answer
        fields=['pk', 's_pk','q_pk','answer','st_pk']
     