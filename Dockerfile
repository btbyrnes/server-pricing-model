
# run command
# docker run -d --name server-pricing-model -p 80:80 server-pricing-model

FROM tiangolo/uwsgi-nginx-flask:python3.6

LABEL maintainer="Brett Byrnes, brettbyrnes@gmail.com" \ 
    description="basic tiangolo/uswgi-niginx-flask app \
    that copies a model into a flask application \
    to serve as an api"

RUN apt-get update

RUN pip install Flask==1.1.2

RUN pip install scikit-learn==0.23.2

RUN pip install pandas==1.1.1

RUN pip install numpy==1.19.1

WORKDIR /app

COPY ./app /app

RUN pip --no-cache-dir install -r /app/requirements.txt

EXPOSE 80