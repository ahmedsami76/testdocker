# this is to pull python image
FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY hello.py .

EXPOSE 5000

CMD python hello.py