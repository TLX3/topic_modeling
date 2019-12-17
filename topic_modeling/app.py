from flask import Flask, request, jsonify
from flask_cors import CORS
from os.path import dirname, realpath
from os import listdir
from analyze_documents import build_lda_model

app = Flask(__name__)
CORS(app)


def json_response(status_code, data):
    res = jsonify(data)
    res.status_code = status_code
    return res


@app.route('/get_CIKs', methods=['GET'])
def available_CIKs():
    path = dirname(realpath(__file__)) + "/data/14d9"
    CIKs = listdir(path)
    return json_response(200, CIKs)


@app.route('/get_topics', methods=['GET'])
def get_topics():
    CIKs = request.args.getlist('CIKs')
    return json_response(200, build_lda_model(CIKs))


if __name__ == '__main__':
    app.run()