# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY weather.py .

# Expose port 5000
EXPOSE 5000

# Define the default command to run the script
#CMD ["gunicorn", "--bind", "0.0.0.0:1000" "weather.py"]
CMD ["python", "weather.py"]
