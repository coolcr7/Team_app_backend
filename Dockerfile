# Base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /backend

# Copy the requirements file to the working directory
#COPY requirements.txt .

# Install the Python dependencies
#RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
#COPY . .

# Expose the port on which the application will run
EXPOSE 8000

# Run the backend application
CMD ["python", "backend.py"]
