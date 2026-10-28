# Use a Python base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies first so Docker can cache this layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Start the API server by default
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
