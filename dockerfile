FROM python:latest

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# expose port 8000 for us to use
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]