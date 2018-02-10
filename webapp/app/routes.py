from app import app
from flask import Flask, render_template, request

@app.route('/')
@app.route('/templates/index')
def index():
    return render_template('index.html')
