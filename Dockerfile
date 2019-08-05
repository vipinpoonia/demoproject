FROM python:3.6

ADD . /demoproject
WORKDIR /demoproject
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y supervisor

COPY setup/supervisor.conf /etc/supervisor/conf.d/
ENTRYPOINT ["supervisord"]
