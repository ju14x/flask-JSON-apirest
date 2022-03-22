import httpx
from flask import Flask, request, jsonify
from flask_pydantic_spec import (
    FlaskPydanticSpec, Response, Request
)

app = Flask(__name__)
spec = FlaskPydanticSpec('flaskinho', title='Flaskinho API REST')
spec.register(app)  # registering endpoints

url = 'https://jsonplaceholder.typicode.com/todos'


@app.get('/')
def five_first_JSONs():
    """Returns first five JSONs from external API"""
    result = httpx.get(url)
    todo_list = result.json()
    todo_data = todo_list[0:5]
    return jsonify(todo_data)
        

if __name__ == '__main__':
    app.run()
