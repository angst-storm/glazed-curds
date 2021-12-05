import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from matrix_creator import get_correspondense_matrix

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@cross_origin()
@app.route('/')
def index():
    get_correspondense_matrix(datetime.datetime.fromtimestamp(int(request.args.to_dict()['date'])))
    return jsonify(request.args.to_dict())


if __name__ == "__main__":
    app.run()
