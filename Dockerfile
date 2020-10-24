# set base image (host OS)
FROM python:3.6

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

# command to run on container start
CMD [ "python3", "./http-server.py", "--host=0.0.0.0"]