import logging

import httpx
from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)
spec = FlaskPydanticSpec('flaskinho', title='Flaskinho API REST')
spec.register(app)  # registering endpoints in OpenAPI/Swagger

url = 'https://jsonplaceholder.typicode.com/todos/'


@app.get('/')
def get_five():
    """Returns first five JSONs from external API"""
    r = httpx.get(url)
    data = r.json()[0:5]
    return jsonify(data)


logging.basicConfig(
    filename='record.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format=f'--------\n %(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
)

if __name__ == '__main__':
    app.run()
