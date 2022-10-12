FROM python:3.9.1

COPY requirements.txt /opt

RUN pip install -r /opt/requirements.txt

COPY app.py /opt

COPY application /opt/application

WORKDIR /opt

CMD flask run --host 0.0.0.0
