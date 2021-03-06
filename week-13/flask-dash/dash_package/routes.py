from flask import render_template, request

from dash_package.dashboard import app

from dash_package.functions import *

@app.server.route('/dash')
def dashboard():
    return app.index()

@app.server.route('/hello')
def hello():
    return "Oh hello"


@app.server.route('/model', methods = ['GET'])
def render_html():
    return render_template('classifier.html')

@app.server.route('/model', methods = ['POST'])
def predict():
    text = request.form.get('name')
    prediction = classify_text(text)
#version 1
    # return str(prediction)

# version 2
    if prediction == 0:
        return render_template('art.html')
    if prediction == 1:
        return render_template('programming.html')
