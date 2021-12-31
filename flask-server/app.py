from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
from pymongo import MongoClient

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/api/btc')
@cross_origin()
def btc():
    btc_state = list(db.btcdb.find({}, {'_id': False}))
    return jsonify({'btc_state': btc_state})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
