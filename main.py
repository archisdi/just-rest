from flask import Flask, jsonify, make_response
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
    app.run(debug=True, host='0.0.0.0', port=5001)
