import joblib

"""
@requires: list containing features of face containing current emotions
@functionality: This function predict emotion of face through trained model
@effect: Return mood of person
"""
def predict(Test):
    filename = 'Model.sav' #if we want to use landmark algorithm model
    #filename = 'combine.sav'
    loaded_model = joblib.load(filename)
    mood = loaded_model.predict([Test])
    return mood



