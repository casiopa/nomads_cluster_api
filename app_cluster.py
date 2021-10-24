from flask import Flask, request, jsonify
from joblib import load
import pandas as pd


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
	return "<h1>Nomads Spain app</h1><p>Clustering users api.</p>"


@app.route('/cluster', methods=['GET'])
def api_cluster():
    new_user = pd.DataFrame.from_dict(request.get_json()['interests'], orient='index').T
    new_user = new_user.reindex(columns = ['climbing', 'fitness', 'football', 'paddle', 'running', 'surf',
                                        'trecking', 'volley', 'bookstores', 'concerts', 'guidedVisits',
                                        'movies', 'museums', 'parks', 'ruralTourism', 'theaters', 'burguers',
                                        'chinese', 'indian', 'italian', 'mediterranean', 'sushi', 'coffee',
                                        'drinks', 'parties', 'sunsets'])
    new_user = new_user.astype('int')
    _id = request.get_json()['_id']

    cluster = model.predict(new_user)
    cluster = int(cluster[0])
    print(cluster)

    return jsonify({"_id": _id, "cluster": cluster})

if __name__ == '__main__':
    model = load('model/model.pkl')
    app.run(debug=True)