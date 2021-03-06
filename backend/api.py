from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from datetime import datetime
from matrix_creator import get_correspondense_matrix

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@cross_origin()
@app.route('/')
def index():
    return jsonify(
        get_correspondense_matrix(
            datetime.fromtimestamp(
                int(request.args.to_dict()['date']))))


if __name__ == "__main__":
    app.run()
