FROM python:3.13.1-slim

RUN apt-get update
RUN apt-get install -y bash

SHELL ["/bin/bash", "-c"]

WORKDIR /home/dolphin/EndpointsJSON
RUN mkdir ./src
COPY install.sh endpoints.json LICENSE pyproject.toml README.md dependencies.txt .
COPY ./src ./src


RUN apt-get install -y tk
RUN ./install.sh

CMD ["/bin/bash", "-c", "source .virtual-environment/bin/activate && python3 src/app.py"]