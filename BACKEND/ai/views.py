from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
import re, json, time
from . import mymattermost
import hashlib
from surveys.models import Survey
from accounts.models import Student
from urllib import parse
# from .telegrambot import main
# Create your views here.
p = re.compile("(대전|광주|구미|서울)_[0-1]{0,1}[0-9]반_[가-힣]+")
q = re.compile("[가-힣]+")
# bot = telegram.Bot(token='1179365738:AAHMVXyhgoxflhquRu3vs7K442KIkteHxDE')

region_ = re.compile("(대전|광주|구미|서울)")
class_ = re.compile("[0-1]{0,1}[0-9]")
name_ = re.compile("[가-힣]+")

@api_view(['POST'])
def send_alert(request):
    students_list = request.data
    text = '님 아침설문 해주세요~~~'
    for students in students_list:
        student_region = region_.match(students).group()
        student_class = class_.search(students).group()
        student_name = name_.findall(students)[-1]
        student_hash = hashlib.sha224(students.encode('utf-8')).hexdigest()
        s_pk = Survey.objects.all().last().pk
        s_pk_hash = hashlib.sha224(str(s_pk).encode('utf-8')).hexdigest()
        s_num = Student.objects.get(class_num=int(student_class), name=student_name, region=student_region).s_num
        s_num_hash = hashlib.sha224(str(s_num).encode('utf-8')).hexdigest()
        survey_url = 'http://i3b108.p.ssafy.io/response/alert?name={}&s_pk={}&s_num={}'.format(student_hash, s_pk_hash, s_num_hash)
        mymattermost.sendmessage(students, student_name + text + '\n' + survey_url)
    return HttpResponse('asdf')

def test(request):
    # print('request start@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    # print(json.loads(request.body.decode('utf8')))
    # print('request end@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    # print(Survey.objects.all().last().pk)
    student = request.body.decode('utf8')
    student = parse.unquote(student)
    student = p.search(student)
    if student:
        student = student.group()
    else:
        print("The format is wrong")
        return HttpResponse("The format is wrong")
    student_region = region_.match(student).group()
    student_class = class_.search(student).group()
    student_name = name_.findall(student)[-1]
    
    with open('ai/attendence.json', 'r') as fp:
        attendence = json.load(fp)
    fp.close()

    if student not in attendence:
        print("not in mm db")
        return HttpResponse("not in mm db")

    if time.time() - attendence['last_attend'] > 43200:
        for k in attendence.keys():
            attendence[k] = 0
        attendence['last_attend'] = time.time()

    if attendence[student]:
        print("already attended")
        return HttpResponse("already attended")
    print(student)
    if not Student.objects.filter(class_num=int(student_class)).filter(name=student_name).filter(region=student_region).count():
        return HttpResponse("not in student db")


    attendence[student] = 1
    student_hash = hashlib.sha224(student.encode('utf-8')).hexdigest()
    s_pk = Survey.objects.all().last().pk
    s_pk_hash = hashlib.sha224(str(s_pk).encode('utf-8')).hexdigest()
    s_num = Student.objects.get(class_num=int(student_class), name=student_name, region=student_region).s_num
    s_num_hash = hashlib.sha224(str(s_num).encode('utf-8')).hexdigest()
    survey_url = 'http://i3b108.p.ssafy.io/response/alert?name={}&s_pk={}&s_num={}'.format(student_hash, s_pk_hash, s_num_hash)
    send_message = '좋은 아침입니다. 아침 설문 부탁드립니다.\n' + survey_url

    
    with open('ai/jsontable.json', 'r') as fp:
        jsontable = json.load(fp)
    fp.close()
    jsontable[s_pk_hash] = s_pk
    jsontable[s_num_hash] = s_num
    jsontable[student_hash] = student_name
    with open('ai/jsontable.json', 'w') as fp:
        json.dump(jsontable, fp)
    fp.close()



    with open('ai/attendence.json', 'w') as fp:
        json.dump(attendence, fp)
    fp.close()
    mymattermost.sendmessage(student, send_message)
    print("process succeed")
    return HttpResponse("process succeed")


# def regist(request):
#     main.register_all()
#     return JsonResponse({"regist": True})
