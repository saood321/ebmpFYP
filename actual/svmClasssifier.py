import pandas as pd
import joblib
import os

def predict(Test):
    #filename = 'Model.sav' if we want to use landmark algorithm model
    filename = 'hog.sav'
    loaded_model = joblib.load(filename)
    var = loaded_model.predict([Test])
    return var



