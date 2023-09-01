FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y nginx nodejs npm
RUN apt-get clean 
RUN rm -rf /var/lib/apt/lists/*

RUN npm install -g mjml

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY nginx.conf /etc/nginx/sites-available/default

COPY . /app
WORKDIR /app
ENV IS_DOCKER_BUILD=true
RUN python manage.py collectstatic
ENV IS_DOCKER_BUILD=false
RUN chmod +x entrypoint.sh


ENV DJANGO_DEBUG=false

EXPOSE 80
ENTRYPOINT ["./entrypoint.sh"]