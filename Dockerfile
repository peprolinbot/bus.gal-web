FROM python:3.10-slim
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
RUN chmod +x entrypoint.sh

ENV DJANGO_DEBUG=false
ENTRYPOINT ["./entrypoint.sh"]