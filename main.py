from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/', methods=['GET'])
def hello():
    return jsonify(msg='Hello Belem!')

@app.route('/index', methods=['GET', 'POST'])
@cross_origin(origin='*', headers=['Content- Type','Accept'])
def index():
    return jsonify(msg='Hello Index!')

app.run(host='0.0.0.0' ,port=8000, debug=True)
