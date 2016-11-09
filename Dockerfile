FROM debian:latest

RUN apt-get update
RUN apt-get install -y python python-dev
RUN apt-get install -y python-pip
RUN pip install locustio

ADD locustfile.py /locustfile.py

ADD run.sh /run.sh

RUN [ "chmod", "755", "run.sh" ]

EXPOSE 8089

CMD ["/run.sh"]