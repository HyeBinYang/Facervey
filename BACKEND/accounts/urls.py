from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'accounts'


urlpatterns = [
    #학생등록
    path('register/student/',views.register_student),
    #학생들가져오기
    path('list/student/', views.list_student),
    path('get/student/', views.student_detail),
    path('update/student/',views.update_student),
    path('delete/student/',views.delete_student),
    path('test/',views.test),
]