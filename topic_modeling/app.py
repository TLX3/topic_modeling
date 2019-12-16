from flask import Flask, request, jsonify
from flask_cors import CORS
from os.path import dirname, realpath
from os import listdir, environ
from analyze_documents import build_lda_model

app = Flask(__name__)
CORS(app)


@app.route('/get_CIKs', methods=['GET'])
def available_CIKs():
    path = dirname(realpath(__file__)) + "/data/14d9"
    CIKs = listdir(path)
    return jsonify(CIKs=CIKs)


@app.route('/get_topics', methods=['GET'])
def get_topics():
    return jsonify(results=build_lda_model(['100412', '1011657', '1009463', '1009356', '1002388', '101063']))


if __name__ == '__main__':
    app.run()
