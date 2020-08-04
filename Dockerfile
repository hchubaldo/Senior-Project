ARG PARENT_IMAGE
FROM ${PARENT_IMAGE}


ARG PARENT_IMAGE

# Recursivly create app directory
RUN mkdir -p /app/data

# Install python dependencies
COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

# Copy app and data
WORKDIR /app

COPY /data ./data
COPY hcorado_SP.py .
