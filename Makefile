.PHONY: build run

# Project Settings
PROJECT_NAME=senior-project
VERSION=0.1.0

# Docker Settings
PARENT_IMAGE=python:3.8-slim
IMAGE=$(PROJECT_NAME):$(VERSION)

build:
	@docker build \
	--build-arg PARENT_IMAGE=$(PARENT_IMAGE) \
	--tag $(IMAGE) \
	.

run: build
	@docker run -it $(IMAGE) python hcorado_SP.py
