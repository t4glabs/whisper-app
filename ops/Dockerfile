# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install whisperx from GitHub
RUN pip install git+https://github.com/m-bain/whisperx.git

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the command to start the Streamlit app
CMD ["streamlit", "run", "src/main.py", "--server.port", "8080"]