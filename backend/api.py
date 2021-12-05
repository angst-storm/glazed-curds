from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@cross_origin()
@app.route('/')
def index():
    print(request.args.to_dict())
    return jsonify(request.args.to_dict())


if __name__ == "__main__":
    app.run()
