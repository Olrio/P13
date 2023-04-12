FROM python:latest

ARG django_secret_key

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV ALLOWED_HOSTS=["*"]
ENV PORT=8000
ENV DJANGO_SECRET_KEY=$django_secret_key

ADD . /app/

WORKDIR /app

RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
