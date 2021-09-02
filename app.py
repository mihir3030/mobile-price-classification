import numpy as np
import flask
from flask import Flask, request, jsonify, render_template
import pickle
import joblib

model = pickle.load(open('model.pkl','rb'))
scaler = joblib.load('Scaler.pkl')

app = flask.Flask(__name__, template_folder='template')

# main index page route
@app.route('/')

def home():
    return render_template('index3.html')



@app.route('/predict',methods=['POST'])
def predict():
    features = [int(x) for x in request.form.values()]
    print(features)
    final_feat = [np.array(features)]
    print(final_feat)
    print(len(final_feat))
    prediction = model.predict(final_feat)
    if prediction == 0:
        mob_pred = 'Rs500 - Rs10,000'
    elif prediction == 1:
        mob_pred = 'Rs 10,000 - Rs 30,000'
    elif prediction == 2:
        mob_pred = 'Rs 30,000 - Rs 60,000'
    elif prediction == 3:
        mob_pred = 'Rs 60,000 - Rs 1,00,000'
    return render_template('index3.html', prediction_text = 'Price Score is {}'.format(mob_pred))

if __name__ == "__main__":
    app.run(debug=True)