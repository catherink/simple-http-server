# set base image (host OS)
FROM ubuntu:18.04

RUN apt update -y
RUN apt install -y python3-pip

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

ENTRYPOINT [ "python3" ]

CMD [ "http-server.py" ]
