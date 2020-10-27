# set base image (host OS)
FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install -y apt-utils
RUN apt-get install -y python3-pip

# set the working directory in the container
WORKDIR /simple-http-server

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

# expose the necessary port
EXPOSE 5000

# copy the content of the local src directory to the working directory
COPY app/ .

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENV FLASK_APP=http-server.py
ENV FLASK_RUN_HOST=0.0.0.0

ENTRYPOINT [ "flask" ]

CMD [ "run" ]
