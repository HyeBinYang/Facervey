# import mattermost
# import re
import json

# mm = mattermost.MMApi('https://meeting.ssafy.com/api')
# mm.login(login_id='ho0707@naver.com', password='Sho0707@naver.com3')
# a = re.compile('대전|광주|구미|서울')
# b = re.compile('[0-1]{0,1}[0-9]반')
# c = re.compile('[가-힣]+')
# students = {}
# for user in mm.get_users():
#     print(user['nickname'])
#     destination = user['nickname']
#     x = a.search(destination)
#     y = b.search(destination)
#     z = c.findall(destination)
#     for i in z:
#         if i != '반' and i != '대전' and i != '광주' and i != '구미' and i != '서울':
#             z = i
#             break
    
#     print(x)
#     print(y)
#     print(z)
#     print('---')
#     if x and y and z:
#         students['{}_{}_{}'.format(x.group(), y.group(), z)] = user['id']
# with open('students.json', 'w') as fp:
#     json.dump(students, fp)
# fp.close()
# for k, v in students.items():
#     students[k] = 0
with open('attendence.json', 'r') as fp:
    students = json.load(fp)
fp.close()
students['last_attend'] -= 43200
with open('attendence.json', 'w') as fp:
    json.dump(students, fp)
fp.close()