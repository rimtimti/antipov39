FROM python:3.10.14-alpine3.19

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

SHELL [ "/bin/bash", "-c" ]

RUN pip install --upgrade pip

COPY requirements.txt /temp/requirements.txt
COPY app /app

RUN useradd -rms /bin/bash app-user && chmod 777 /opt /run

WORKDIR /app

RUN mkdir /app/static && chown -R app-user:app-user /app && chmod 755 /app

EXPOSE 8000

RUN pip install -r /temp/requirements.txt

USER app-user