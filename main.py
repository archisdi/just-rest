from dotenv import load_dotenv
from flask import Flask, jsonify, make_response
from os import getenv, path

load_dotenv(path.join(path.dirname(__file__), '.env'))
app = Flask(__name__)


@app.route('/')
def handler():
    return make_response(
        jsonify({
            'message': 'a response message',
            'data': None
        })
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=getenv('APP_PORT'))
