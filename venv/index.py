from flask import Flask, request, redirect, url_for, flash, jsonify, render_template
import numpy as np
import pickle as p
import json
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

messages = [{'genre': 'Message One',}]
modelfile = 'model.pickle'
model = p.load(open(modelfile, 'rb'))

@app.route("/")
def index():
    return render_template('index.html', messages=messages)

@app.route('/', methods=('GET', 'POST'))
def result():
    if request.method == 'POST':
        lyric = request.form['lyric']
        if not lyric:
            flash('lyric is required!')
        else:
            prediction = np.array2string(model.predict([lyric]))
            messages.append({'genre': prediction})
            return redirect(url_for('index'))
    return render_template('index.html', messages=messages)

@app.route('/api/', methods=['POST'])
def get_calc():
    data = request.get_json(force=True)
    prediction = np.array2string(model.predict([data['lyric']]))
    return jsonify(prediction)

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

if __name__ == '__main__':
    modelfile = 'model.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')
