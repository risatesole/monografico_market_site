# Base image
FROM python:3.12-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apk add --no-cache build-base libffi-dev musl-dev mariadb-client bash

# Set work directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

# Expose default Django port
EXPOSE 8000

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

###########################################################
# Podman Instructions:
#
# 1. Build the image:
#    podman build -t django-app .
#
# 2. Run the container using your environment file:
#    podman run --env-file .env.example django-app
#
# 3. Optional: map port if you want to access Django from the host:
#    podman run -p 8000:8000 --env-file .env.example django-app
###########################################################
