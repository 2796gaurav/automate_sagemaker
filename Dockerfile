FROM python:3.8

COPY requirements.txt /usr/bin/requirements.txt

RUN pip3 install -r /usr/bin/requirements.txt

COPY src/training-script.py /usr/bin/train
COPY src/serve-script.py /usr/bin/serve

RUN chmod 755 /usr/bin/train /usr/bin/serve

EXPOSE 8080