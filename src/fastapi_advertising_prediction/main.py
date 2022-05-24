import os
import pathlib
from fastapi import FastAPI
from fastapi_advertising_prediction.schemas import Advertising
import joblib

# Read models saved during train phase
current_dir = pathlib.Path(__file__).parent.resolve()
dirname = os.path.join(current_dir, 'saved_models')
estimator_advertising_loaded = joblib.load(os.path.join(dirname,"03.randomforest_with_advertising.pkl"))

app = FastAPI()

def make_advertising_prediction(model, request):
    # parse input from request
    TV = request["TV"]
    Radio = request['Radio']
    Newspaper = request['Newspaper']

    # Make an input vector
    advertising = [[TV, Radio, Newspaper]]

    # Predict
    prediction = model.predict(advertising)

    return prediction[0]

# Advertising prediction endpoint
@app.post("/prediction/advertising")
def predict_iris(request: Advertising):
    prediction = make_advertising_prediction(estimator_advertising_loaded, request.dict())
    return {"result": prediction}