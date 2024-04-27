# Dockerfile for Django app

# Use the official Python image as the base image
FROM python:3.10


# Set the working directory in the container
WORKDIR /app/booking_system

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt


# Copy the Django project files to the container
COPY . .   


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1





