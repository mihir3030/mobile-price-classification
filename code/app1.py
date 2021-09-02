import flask
from flask import request, render_template
import joblib
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

app = flask.Flask(__name__, template_folder='template')

#app.config["DEBUG"] = True

# main index page route
@app.route('/')

def home():
    return render_template('index1.html')


@app.route('/predict',methods=['POST'])
def predict():
    scaler = joblib.load('Scaler.pkl')
    model = joblib.load('mobile-price-prediction.pkl')
    int_features = [float(x) for x in request.form.values()]
    x = [np.array(int_features)]
    # #xx = scaler.transform(x)
    pred = model.predict(x)
    output = round(pred[0],0)
     
    if output == 0:
        mob_pred = 'Rs500 - Rs10,000'
    elif output == 1:
        mob_pred = 'Rs 10,000 - Rs 30,000'
    elif output == 2:
        mob_pred = 'Rs 30,000 - Rs 60,000'
    elif output == 3:
        mob_pred = 'Rs 60,000 - Rs 1,00,000'
    return render_template('index1.html',prediction = "Mobile Price Prediction is: {}" .format(mob_pred))


# app.run(debug = True)

if __name__ == '__main__':
	app.run(debug=True)                          
