FROM cutejaeho/python3.7.3:1.0 
ENV PYTHONUNBUFFERED 1
RUN mkdir django
VOLUME /django

ADD . /django
WORKDIR /django
RUN chmod 755 /django/start  
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install python-telegram-bot
RUN pip install mattermost

EXPOSE 8000

ENTRYPOINT ["./start"]
