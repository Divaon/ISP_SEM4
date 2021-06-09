FROM python:3.8
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt ./web_django/
WORKDIR /web_django
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
