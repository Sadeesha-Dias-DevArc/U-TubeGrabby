FROM python:3.10 

WORKDIR /app

# Install project dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy application and video files
COPY . .

# Expose port (adjust if needed)
#EXPOSE 8000

# Set your application entry point
CMD ["python", "src/main.py"]  # Replace with your actual entry point script

# This line copies videos to a writable volume:
VOLUME ["/videos"]
