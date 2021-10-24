from flask import Flask, request, jsonify
from joblib import load
import pandas as pd
from distutils.util import strtobool
from sklearn.cluster import KMeans


app = Flask(__name__)
# app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
	return "<h1>Nomads Spain app</h1><p>Clustering users api.</p>"


@app.route('/cluster', methods=['GET'])
def api_cluster():
    new_user = pd.DataFrame.from_dict(request.get_json(), orient='index').T
    user_id = new_user['user_id'].values[0]
    new_user.drop('user_id', axis='columns', inplace=True)
    new_user = new_user.applymap(strtobool)

    cluster = model.predict(new_user)
    cluster = int(cluster[0])
    print(cluster)

    return jsonify({'user_id': user_id, 'cluster': cluster})

if __name__ == '__main__':
    model = load('model/model.pkl')
    app.run(debug=True)