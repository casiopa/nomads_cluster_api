from flask import Flask, request, jsonify
from joblib import load
import pandas as pd


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
	return "<h1>Nomads Spain app</h1><p>Clustering users api.</p>"


@app.route('/cluster', methods=['GET'])
def api_cluster():

    _id = request.get_json()['_id']



    return jsonify({"_id": _id})

if __name__ == '__main__':
    model = load('model/model.pkl')
    app.run(debug=True)