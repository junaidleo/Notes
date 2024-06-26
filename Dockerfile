FROM python:3.9

WORKDIR /tmp

COPY ./requirements.txt /tmp/requirements.txt
COPY ./.env /tmp/.env

RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY ./app /tmp/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]