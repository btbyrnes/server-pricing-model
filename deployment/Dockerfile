
# run command
# docker run -d --name server-pricing-model -p 80:80 server-pricing-model

FROM tiangolo/uwsgi-nginx-flask:python3.6

LABEL maintainer="Brett Byrnes, brettbyrnes@gmail.com" \ 
    description="basic tiangolo/uswgi-niginx-flask app \
    that copies a model into a flask application \
    to serve as an api"

RUN apt-get update

WORKDIR /app

COPY ./app /app

RUN pip --no-cache-dir install -r /app/requirements.txt

EXPOSE 80 443