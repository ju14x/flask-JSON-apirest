from datetime import datetime
import logging

import httpx
from flask import Flask, jsonify
from flask_pydantic_spec import (FlaskPydanticSpec)

app = Flask(__name__)
spec = FlaskPydanticSpec('flaskinho', title='Flaskinho API REST')
spec.register(app)  # registering endpoints

url = 'https://jsonplaceholder.typicode.com/todos/'

logging.basicConfig(
    filename='record.log',
    encoding='utf-8', 
    level=logging.DEBUG, 
    format = f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S'
)


@app.get('/')
def get_five():
    """Returns first five JSONs from external API"""
    r = httpx.get(url)
    data = r.json()[0:5]
    return jsonify(data)


if __name__ == '__main__':
    app.run()
