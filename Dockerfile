FROM python:3.10-alpine as builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update \
    && apk add --no-cache \
    build-base \
    libffi-dev \
    postgresql-dev \
    gcc \
    musl-dev \
    linux-headers \
    pcre-dev

WORKDIR /app

COPY projeto/requirements.txt .

RUN python -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY projeto .

FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --no-cache libpq

WORKDIR /app

COPY projeto .

COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY .env /app/.env

RUN python manage.py collectstatic --noinput

EXPOSE 8000

COPY commands.sh /app/commands.sh
RUN chmod +x /app/commands.sh

CMD ["/app/commands.sh"]