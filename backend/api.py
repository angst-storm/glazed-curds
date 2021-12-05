from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(request.args.to_dict())


if __name__ == "__main__":
    app.run()
