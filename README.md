Ideally it should be Helm chart deployed to Minikube, in fact it can run with Docker compose. Healthcheck will be found in /health path, when server is running. Docker compose will not have any changes to server's code included, as it takes ready image. If some changes are made to server's code and you want to see them live, Docker compose file should be changed to build new image from Dockerfile.
