FROM python:3

COPY ./application /opt/application
WORKDIR /opt/application

RUN pip install flask redis

CMD python app.py
