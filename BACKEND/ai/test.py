import re, json, time
import mymattermost
import os
# from .telegrambot import main
# Create your views here.
p = re.compile("(대전|광주|구미|서울)_[0-1]{0,1}[0-9]반_[가-힣]+")
q = re.compile("[가-힣]+")
# bot = telegram.Bot(token='1179365738:AAHMVXyhgoxflhquRu3vs7K442KIkteHxDE')
region_ = re.compile("대전")
class_ = re.compile("(6반)")
name_ = re.compile("(민강규|공필상|김가람|김동욱|김무성|김송희|김준호|김지연|김태인|김형래|김호준|박인남|박주현|박진용|박현우|배상은|심동식|정영진|윤동현|이상호|이연재|이영복|이태경|이태환|김인호|임승현|정성오|정인균|정진아|조수미|최환석|한창희|나호철|황규진|황호민|조희진|엄홍재)")
# text = '안녕하세요. 저는 8조 팀원 김원호입니다. 저희가 얼굴인식을 통해서 출결처리와, 설문지를 매터모스트로 보내는 프로젝트를 하고 있는데요. 혹시 괜찮으시면 내일 시연 때 에듀싸피 우리 반 보기에 있는 사진 사용해도 될까요?'
with open('students.json', 'r') as fp:
    students = json.load(fp)
fp.close()
arr = []
for k,v in students.items():
    region_daejeon = region_.search(k)
    class_1or4 = class_.search(k)
    name_our = name_.search(k)
    if region_daejeon and class_1or4 and name_our:
        print(k)