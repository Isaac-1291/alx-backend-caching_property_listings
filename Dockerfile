# 1. Start from a Python image
FROM python:3.12-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5. Copy your Django project files
COPY . .

# 6. Expose Django's default port
EXPOSE 8000

# 7. Start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]