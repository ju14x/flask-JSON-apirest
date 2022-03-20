from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)
spec = FlaskPydanticSpec('flaskinho', title='Flaskinho API REST')
spec.register(app)  # registering app's endpoints


@app.route('/')
def get_data():
    return 'oi'

app.run()
