FROM python:3.7-slim-buster

COPY requirements.txt /usr/bin/requirements.txt

RUN pip3 install -r /usr/bin/requirements.txt


ENV PYTHONUNBUFFERED=TRUE

ENTRYPOINT ["python3"]