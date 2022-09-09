#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Web App with Python Flask!'



@app.route('/', methods=['POST'])
def my_command():
    if request.json["type"] == 1:
        return jsonify({
            "type": 1
        })


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)