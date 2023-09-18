FROM python:3.10 AS base

WORKDIR /api
COPY requirements.txt /api/
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY . /api/

FROM base AS development
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM base AS production
CMD ["gunicorn", "--bind", "0.0.0.0:8000"]