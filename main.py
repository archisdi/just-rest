from dotenv import load_dotenv
from flask import Flask
from utils import api_response
from os import getenv, path

load_dotenv(path.join(path.dirname(__file__), '.env'))
app = Flask(__name__)

@app.route('/')
def handler():
    return api_response({'message': 'a response message', 'data': None })

if __name__ == '__main__':
    app.run(debug=getenv('APP_DEBUG') == "true", host='0.0.0.0', port=getenv('APP_PORT'))
