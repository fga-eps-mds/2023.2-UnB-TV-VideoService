FROM python:3.10.9-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY . .

RUN apt-get update
RUN apt-get -y install libpq-dev gcc 

ENV PYTHONPATH "/app/src"
RUN pip install -r requirements.txt
 
EXPOSE 8081

CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0","--port", "8081","--reload"]