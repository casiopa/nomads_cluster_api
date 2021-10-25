from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from joblib import load
import pandas as pd


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

model = load('model/model.pkl')


@app.route('/', methods=['GET'])
def home():
	return "<h1>Nomads Spain app</h1><p>Clustering users api.</p>"


@app.route('/cluster', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type'] , methods=['GET'])
def api_cluster():
    new_user = pd.DataFrame.from_dict(request.get_json(force=True)['interests'], orient='index').T
    new_user = new_user.reindex(columns = ['climbing', 'fitness', 'football', 'paddle', 'running', 'surf',
                                        'trecking', 'volley', 'bookstores', 'concerts', 'guidedVisits',
                                        'movies', 'museums', 'parks', 'ruralTourism', 'theaters', 'burguers',
                                        'chinese', 'indian', 'italian', 'mediterranean', 'sushi', 'coffee',
                                        'drinks', 'parties', 'sunsets'])
    new_user = new_user.astype('int')
    print(new_user.columns)
    _id = request.get_json(force=True)['_id']

    cluster = int(model.transform(new_user).argmax())
    print(cluster)

    return jsonify({"_id": _id, "cluster": cluster})

if __name__ == '__main__':
    app.run()