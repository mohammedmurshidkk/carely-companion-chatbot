# Use official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt ./

# Fix dependency issues and install packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir huggingface_hub==0.20.3 && \
    pip install --no-cache-dir sentence-transformers==2.2.2 && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
