ARG PARENT_IMAGE
FROM ${PARENT_IMAGE}


ARG PARENT_IMAGE

# Recursivly create app directory
RUN mkdir -p /app/data
RUN mkdir -p gcc

# Install Linux packages
RUN apt-get update -y
RUN apt-get install -y apt-utils
RUN apt-get install -y pkg-config
RUN apt-get install -y libcairo2-dev

# Install python dependencies
COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

# Copy app and data
WORKDIR /app

COPY /data ./data
COPY hcorado_SP.py .
COPY hh_script.py .
