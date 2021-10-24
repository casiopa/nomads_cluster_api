from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return "<h1>Nomads Spain app</h1><p>Clustering users api.</p>"

@app.route('/cluster', methods=['GET'])
def api_cluster():
    user_id = int(request.get_json()['user_id'])
    surf = int(bool(request.get_json()['Surf']))

    return jsonify({'user_id': user_id, 'cluster': random.randint(0,5), 'surf': surf})

if __name__ == '__main__':
    app.run(debug=True)