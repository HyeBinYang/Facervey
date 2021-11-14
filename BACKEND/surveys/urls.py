from django.urls import path
from . import views

app_name = 'surveys'

urlpatterns =[
     path('check/student/',views.do_or_not),
     path('statistics/',views.get_result_survey_student),
     path('delete/answer/student',views.tmp),
     path('search/',views.search),
     #설문지 검색하기
     path('list/recent/',views.list_recent_survey),
     #내 설문 리스트 가져오기
     path('list/', views.list_survey),
     #설문 상세보기
     path('detail/', views.detail_survey),
     
     #설문 배경색 바꾸기
     path('color/', views.change_color),     
     #설문지
     path('create/', views.create_survey),
     path('delete/', views.delete_survey),
     path('update/', views.update_survey),
     #질문
     path('list/question/',views.list_question),
     path('create/question/', views.create_question),
     path('update/question/', views.update_question),
     path('delete/question/', views.delete_question),
     #옵션
     path('create/option/', views.create_option),
     path('update/option/', views.update_option),
     path('delete/option/', views.delete_option),

     #학생응답
     path('create/answer/student/',views.create_student_answer),
     path('responses/', views.get_result_survey_student),
     path('student/res/', views.get_answers),

     #링크생성
     path('makelink/',views.makelink),
    
]