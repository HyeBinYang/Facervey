from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse  
from .models import Student
from .serializers import StudentSerializer, StudentListSerializer
from django.contrib.sites.models import Site
import json

@api_view(['GET'])
def test(request):
    my_site = Site.objects.all()
    my = Site.objects.get(pk=2)            
    
    print(my_site)
    for i in my_site:
        print(i.id, i.domain, i.name)
    return JsonResponse({"status": 200})
# Create your views here.
@api_view(['POST'])
def register_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        st = Student.objects.all().last()
    return JsonResponse({"st_pk": st.pk})

@api_view(['POST'])
def list_student(request):
    students = Student.objects.filter()
    serializer = StudentListSerializer(students, many=True)    
    return Response(serializer.data)

@api_view(['POST'])
def student_detail(request):
    with open('ai/jsontable.json', 'r') as fp:
        jsontable = json.load(fp)
    fp.close()
    s_num = request.data['s_num']
    if type(s_num) == type(''):
        s_num = jsontable[s_num]
    student = Student.objects.get(s_num=s_num)
    # student = Student.objects.get(s_num=request.data['s_num'])
    serializer = StudentSerializer(student)
    return Response(serializer.data)

@api_view(['POST'])
def update_student(request):
    s = Student.objects.get(pk=request.data['pk'])
    s.s_num = request.data['s_num']
    s.class_num = request.data['class_num']
    s.name = request.data['name']
    s.y_num = request.data['y_num']
    s.region = request.data['region']
    s.save()    
    return JsonResponse({"status":"200"})

@api_view(['POST'])
def delete_student(request):
    s = Student.objects.get(pk=request.data['pk'])
    s.delete()
    return JsonResponse({"status":"200"})
    
