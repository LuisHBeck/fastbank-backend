FROM python:3.11.3-alpine3.18

LABEL mantainer="github.com/LuisHBeck"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY . code/
COPY scripts /scripts

WORKDIR /code

EXPOSE 8000

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /code/requirements.txt && \
  adduser --disabled-password --no-create-home dkuser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R dkuser:dkuser /venv && \
  chown -R dkuser:dkuser /data/web/static && \
  chown -R dkuser:dkuser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts

RUN chmod +x /code/manage.py

ENV PATH="/scripts:/venv/bin:$PATH"

USER dkuser

CMD ["commands.sh"]