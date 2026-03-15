FROM public.ecr.aws/docker/library/python:3.13-slim

# FROM python:3.13-slim

WORKDIR /app

COPY requirements/api.txt /app/requirements/api.txt
RUN pip install --no-cache-dir -r /app/requirements/api.txt

COPY apps/api /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]