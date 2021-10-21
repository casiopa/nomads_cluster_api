from flask import Flask, request, jsonify
import random
 
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/nomad_cluster', methods=['GET'])
def get_by_id():
    user_id = int(request.get_json()['user_id'])
    surf = int(bool(request.get_json()['surf']))

    return jsonify({'user_id': user_id, 'cluster': random.randint(0,5), 'surf': surf})

app.run()