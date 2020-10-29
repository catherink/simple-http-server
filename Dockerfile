# set base image (host OS)
FROM ubuntu:18.04

# installing pip for python3
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

# some env variables without which python3 has encoding issues and container doesn't run
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# declaring environment variables for Flask, telling which script to run and which host to use
ENV FLASK_APP=http-server.py
ENV FLASK_RUN_HOST=0.0.0.0

# default executable
ENTRYPOINT [ "flask" ]

# which command to run with executable
CMD [ "run" ]
