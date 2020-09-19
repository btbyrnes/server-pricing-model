import numpy as np
from sklearn import linear_model

import os

import pickle
import os

model_file = 'model/model.pkl'

with open(model_file,'rb') as f:
    model_saved = pickle.load(f)

def predict_handler(x1,x2,x3,x4):
    x = np.array([float(x1),float(x2),float(x3),float(x4)]).reshape(1,-1)
    return predict(x).item(0)

def predict(X):
    return model_saved.predict(X)
