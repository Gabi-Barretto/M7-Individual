
# Use an official Python runtime as a base image
FROM python:3.8-slim

RUN mkdir /app

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV NAME World

# Run streamlit_app.py when the container launches
CMD ["streamlit", "run", "streamlit_app.py"]
