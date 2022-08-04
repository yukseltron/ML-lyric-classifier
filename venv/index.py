from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Lyrics Classifier</h1>"

@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json(force=True)
    prediction = np.array2string(model.predict(data['lyric']))
    print(prediction)
    return jsonify(prediction)


if __name__ == '__main__':
    modelfile = 'model.pickle'
    model = p.load(open(modelfile, 'rb'))
