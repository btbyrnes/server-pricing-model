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

#model.html
@app.route("/model")
def model_page():
  answer = 5.0
  return render_template('model.html', prediction = '{}'.format(str(answer)))

# health check
# http://home-server.local/api/health-check
@app.route("/api/health-check")
def isAlive():
  return jsonify(status=200)

# route at /predict/q that follows the format of
# http://192.168.1.200/api/predict?speed=2.2&cores=12&storage=2000&ram=32
@app.route("/api/predict")
def predict():

  x1 = request.args['speed']
  x2 = request.args['cores']
  x3 = request.args['storage']
  x4 = request.args['ram']

  print(type(x1), type(x2), type(x3), type(x4))

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

# ## TO DO - ADD THE CODE TO RENDER THE MODEL PAGE
@app.route("/model/predict", methods=['POST'])
def model_predict_page():

  features = list(request.form.values())

  x1 = features[0]
  x2 = features[1]
  x3 = features[2]
  x4 = features[3]

  answer =  model.predict_handler(x1,x2,x3,x4)

  return render_template('model.html', prediction = '${:.2f}'.format(float(answer)))
