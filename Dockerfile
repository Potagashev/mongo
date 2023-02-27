FROM python:3.11

WORKDIR /app/
COPY requirements.txt .
RUN pip install -r requirements.txt

ADD . /app

CMD uvicorn main:app --host 0.0.0.0 --port 80
EXPOSE 8080