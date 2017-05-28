FROM python:3.6.1-slim

ADD . /home/botler-api/
WORKDIR /home/botler-api/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["/home/botler-api/run.sh"] 

EXPOSE 5000
