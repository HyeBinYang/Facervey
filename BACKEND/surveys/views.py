from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse  
from django.db.models import Q, Count
import json
import hashlib
# Create your views here.
from .serializers import (SurveySerializer,QuestionSerializer,MAnswerSerializer,
SurveyListSerializer,QuestionListSerializer,MAnswerListSerializer,StudentAnswerSerializer)
from .models import Survey, Survey_Question, Multiple_Answer, Student_Answer
from accounts.models import User, Student

@api_view(['POST'])
def search(request):
    keyword = request.data['keyword']
    surveys=Survey.objects.filter(Q(user=request.user) & Q(title__contains=keyword))
    serializer = SurveyListSerializer(surveys, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def list_recent_survey(request):
    #가장 최근에 생성된 설문 순서대로 10개를 가져온다.
    surveys = Survey.objects.filter(user=request.user).order_by('-pk')[:10]
    serializer = SurveyListSerializer(surveys, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def list_survey(request):
    surveys = Survey.objects.filter(user=request.user).order_by('-created_at')
    serializer = SurveyListSerializer(surveys, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def detail_survey(request):
    # print(request.data)
    with open('ai/jsontable.json', 'r') as fp:
        jsontable = json.load(fp)
    fp.close()
    pk = request.data['pk']
    if type(pk) == type(''):
        pk = jsontable[pk]
    survey = Survey.objects.get(pk=pk)
    # survey = Survey.objects.get(pk=request.data['pk'])
    serializer1 = SurveySerializer(survey)
    questions = survey.questions.all()
    serializer2 = QuestionListSerializer(questions, many=True)
    answers = Multiple_Answer.objects.filter(s_pk=pk).order_by('q_pk_id')
    serializer3 = MAnswerListSerializer(answers,many=True)
    # print(questions)
    return JsonResponse({"survey":serializer1.data,"questions":serializer2.data,"answers":serializer3.data})
    # serializer1 = SurveySerializer(survey)
    # questions = Survey_Question.objects.filter(s_pk=request.data['pk'])
    # serializer2 = QuestionListSerializer(questions,many=True)
    # answers = Multiple_Answer.objects.filter(s_pk=request.data['pk']).order_by('q_pk_id')
    # serializer3 = MAnswerListSerializer(answers,many=True)

    # return JsonResponse({"survey":serializer1.data,"questions":serializer2.data,"answers":serializer3.data})

@api_view(['POST'])
def create_survey(request):
    serializer = SurveySerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        res = serializer.save(user=request.user)
        sv=Survey.objects.all().last()
        return JsonResponse({ "s_pk": sv.pk })
    return Response(None)

@api_view(['POST'])
def update_survey(request):
    s = Survey.objects.get(pk=request.data['survey']['pk'])
    s.title=request.data['survey']['title']
    s.description=request.data['survey']['description']
    s.color = request.data['survey']['color']
    s.save()    
    return JsonResponse({"status":"200"})

@api_view(['POST'])
def delete_survey(request):
    s = Survey.objects.get(pk=request.data['pk'])
    s.delete()
    return JsonResponse({"status":"200"})

@api_view(['POST'])
def change_color(request):
    s = Survey.objects.get(pk=request.data['s_pk'])
    s.color=request.data['color']

    s.save()    
    return JsonResponse({"status":"200"})

@api_view(['POST'])
def list_question(request): #해당 설문의 질문리스트가져오기
    questions = Survey_Question.objects.filter(pk=request.data['pk'])
    serializer1 = QuestionListSerializer(questions,many=True)
    answers = Multiple_Answer.objects.filter(pk=request.data['pk']).order_by('q_pk_id')
    serializer2 = MAnswerListSerializer(answers,many=True)
    return JsonResponse({"questions":serializer1.data,"answers":serializer2.data})

@api_view(['POST'])
def create_question(request):
    serializer = QuestionSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)        
        sq=Survey_Question.objects.all().last()
        return JsonResponse({"q_pk": sq.pk})

@api_view(['POST'])
def update_question(request):
    q = Survey_Question.objects.get(pk=request.data['pk'])
    q.content=request.data['content']
    q.q_type=request.data['q_type']
    q.save()    
    return JsonResponse({"status":"200"})

@api_view(['POST'])
def delete_question(request):
    q = Survey_Question.objects.get(pk=request.data['pk'])
    q.delete()
    return JsonResponse({"status":"200"})


@api_view(['POST'])
def create_option(request):
    serializer = MAnswerSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        a = Multiple_Answer.objects.all().last()        
        return JsonResponse({"a_pk": a.pk})

@api_view(['POST'])
def update_option(request):
    a = Multiple_Answer.objects.get(pk=request.data['pk'])
    a.content=request.data['content']
    a.save()
    return JsonResponse({"status":"200"})

@api_view(['POST'])
def delete_option(request):
    a = Multiple_Answer.objects.get(pk=request.data['pk'])
    a.delete()
    return JsonResponse({"status":"200"})

@api_view(['POST'])
def create_student_answer(request):
    print(request.data)
    st_pk=request.data['st_pk']
    s_pk=request.data['s_pk']
    for question in request.data['questions']:
        tmp = {}
        q_pk=question['q_pk'] #질문번호
        answer=question['answer'] #대답
        #Student_Answer에 담을것!
        tmp['q_pk']=q_pk
        tmp['answer']=answer
        tmp['st_pk']=st_pk
        tmp['s_pk']=s_pk
        # tmp['s_num']=s_num
        print(tmp)
        serializer = StudentAnswerSerializer(data=tmp)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def tmp(request):
    sta = Student_Answer.objects.filter(st_pk_id=request.data['st_pk'])
    sta.delete()
    return JsonResponse({"status":"200"})
    
#한 설문에 대한 한 학생의 대답을 가져온다.
def get_answer_one_student(request):
    #설문지 번호와 해당 설문에 임한 특정 학생을 필터로 거르고 대답만을 가져온다.
    st_answers = Student_Answer.objects.filter(Q(st_pk=request.data['s_num']) & Q(s_pk=request.data['s_pk']))
    serializer = StudentAnswerSerializer(st_answer, many=True) #대답이들어있을것임
    #해당설문지 내용가져오기.
    survey = Survey.objects.get(pk=request.data['s_pk'])
    serializer1 = SurveySerializer(survey)
    questions = Survey_Question.objects.filter(s_pk=request.data['s_pk'])
    serializer2 = QuestionListSerializer(questions,many=True)
    answers = Multiple_Answer.objects.filter(s_pk=request.data['s_pk']).order_by('q_pk_id')
    serializer3 = MAnswerListSerializer(answers,many=True)
    
    return JsonResponse({"survey":serializer1.data,"questions":serializer2.data,"options":serializer3.data,"answers":serializer.data})

@api_view(['POST'])
def get_answers(request):
    with open('ai/jsontable.json', 'r') as fp:
        jsontable = json.load(fp)
    fp.close()
    x = request.data['s_pk']
    if type(x) == type(''):
        x = jsontable[x]
    # print(jsontable[request.data['s_pk']])
    survey_answers = Student_Answer.objects.filter(s_pk=x)
    # survey_answers = Student_Answer.objects.filter(s_pk=request.data['s_pk'])
    serializer = StudentAnswerSerializer(survey_answers, many=True)
    return Response(serializer.data)

#한 설문에 대한 학생들의 모든 대답을 가져온다.
@api_view(['POST'])
def get_result_survey_student(request):
    qd = {}
    for question in Survey.objects.get(pk=request.data['pk']).questions.all():
        qd[question.pk] = {'q_type': question.q_type}
        diction = question.student_answer_set.all().values('answer').annotate(Count('answer'))
        for d in diction:
            qd[question.pk][d['answer']] = d['answer__count']

    return JsonResponse({"result": qd})

@api_view(['POST'])
def do_or_not(request):
    #student answer에서 응시한 학생들의 set을 가져온다.
    for student in Survey.objects.get(pk=request.data['s_pk']).students.all():
        print(student.y_num, student.region, student.class_num, student.name, student.s_num, student.img)
    
    
    #설문에 응답한 학생만 우선 리턴해준다.
    return JsonResponse({"result": "testing...."})

@api_view(['POST'])
def makelink(request):
    region = request.data['region']
    y_num = request.data['y_num']
    students = Student.objects.filter(Q(region=region) & Q(y_num=y_num))
    for student in students:
        name = hashlib.sha224(str(student.name).encode('utf-8')).hexdigest()
        print(name)
        h2 = str(name).decode('utf-8')
        print(h2)
        s_num = hashlib.sha224(str(student.s_num).encode('utf-8')).hexdigest()
        
        print(s_num)
        
    
    return JsonResponse({"result1": region, "result2":y_num})
