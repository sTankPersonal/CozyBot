# Use official Python image
FROM python:3.13.7

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your bot code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python", "CozyBot.py"]