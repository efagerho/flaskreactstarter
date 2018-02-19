import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_url_path='')

@app.route('/api/v1/hello', methods=['GET'])
def hello():
    return jsonify({'msg': 'Hello World!'})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', ssl_context='adhoc')