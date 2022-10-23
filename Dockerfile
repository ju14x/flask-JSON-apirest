FROM python:3.10.3

RUN pip install --upgrade pip

COPY ./requirements.txt ./.flaskenv ./app.py /app/

WORKDIR /app

RUN pip install -r requirements.txt

CMD flask run -h 0.0.0.0 -p 5000

EXPOSE 5000