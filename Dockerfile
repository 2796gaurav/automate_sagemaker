FROM python:3.8

RUN pip3 install -r requrements.txt

COPY src/training-script.py /usr/bin/train
COPY src/serve-script.py /usr/bin/serve

RUN chmod 755 /usr/bin/train /usr/bin/serve

EXPOSE 8080