# Select an OS
FROM python:3.12.1

# Generate python output ( for example, some logs)
ENV PYTHONUNBUFFERED 1

# create a folder root
RUN mkdir /app-root

# Set the working directory
WORKDIR /app-root

# Copy and link the current directory contents into the container
ADD . /app-root

RUN pip install -r requirements.txt