# Use an official Python runtime as a parent image
FROM python:3.11-alpine

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app 

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
