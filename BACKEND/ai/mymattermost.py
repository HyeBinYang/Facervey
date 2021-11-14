import mattermost
import re, json

def finduser(지역, 반, 이름, username):
    if 지역 in username and 반 in username and 이름 in username:
        return True
    return False

def sendmessage(destination, text):
    mm = mattermost.MMApi('https://meeting.ssafy.com/api')
    mm.login(login_id='ho0707@naver.com', password='Sho0707@naver.com3')
    with open('ai/students.json', 'r') as fp:
        students = json.load(fp)
    fp.close()
    print(destination)
    print(text)
    channel = mm.create_dm_channel_with(students[destination])
    mm.create_post(channel['id'], text)

if __name__ == '__main__':
    pass
