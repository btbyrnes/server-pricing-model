# basic imports
from flask import Flask, jsonify, request, render_template
import os

# model.py import from app/model folder
from model import model

app = Flask(__name__)

print('------------------------------')
print('Brett Byrnes')
print('www.bbyrnes.com')
print('brettbyrnes@gmail.com')
print('')
print('webserver has started')
print('working directory: %s' % os.getcwd())
print('------------------------------')

# index.html
@app.route("/")
def home():
  return render_template('index.html')

# health check
# http://home-server.local/api/health-check
@app.route("/api/health-check")
def isAlive():
  return jsonify(status=200)

# route at /predict/q that follows the format of
# http://home-server.local/api/predict?speed=2.2&cores=12&storage=2000&ram=32
@app.route("/api/predict")
def predict_query():

  x1 = request.args['speed']
  x2 = request.args['cores']
  x3 = request.args['storage']
  x4 = request.args['ram']
  # x's are sent as strings from the query
  # the predict_handler returns the value of y as a number, this will be
  # jsonify'd
  y = model.predict_handler(x1, x2, x3, x4)

  return jsonify(
    speed=x1,
    cores=x2,
    storage=x3,
    ram=x4,
    price=y
  )