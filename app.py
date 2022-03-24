import logging
import httpx

from os import abort
from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)
spec = FlaskPydanticSpec('flaskinho', title='Flaskinho API REST')
spec.register(app)

url = 'https://jsonplaceholder.typicode.com/todos/'


@app.get('/')
def get_five():
    """Returns first five JSONs from external API"""
    r = httpx.get(url)
    data = r.json()[0:5]
    try:
        return jsonify(data)
    except httpx.HTTPStatusError:
        abort(400, 'Bad request')


logging.basicConfig(
    filename='record.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format=f'--------\n %(asctime)s %(levelname)s : %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
)

if __name__ == '__main__':
    app.run()
