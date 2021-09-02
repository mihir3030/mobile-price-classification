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
   

@app.route('/predict',methods=['GET'])
def predict():
    scaler = joblib.load('Scaler.pkl')
    model = joblib.load('mobile-price-prediction.pkl')
    #model = joblib.load('mobile_price_prediction.pkl')
    price_predict = model.predict([[int(request.args['battery_power']),
                            1,
                            3.5,
                            int(request.args['dual_sim']),
                            int(request.args['fc']),
                            int(request.args['four_g']),
                            int(request.args['int_memory']),
                            0.25,
                            int(request.args['mobile_wt']),
                            int(request.args['n_cores']),
                            int(request.args['pc']),
                            int(request.args['px_height']),
                            int(request.args['px_width']),
                            int(request.args['ram']),
                            int(request.args['sc_h']),
                            int(request.args['sc_w']),
                            20,
                            1,
                            int(request.args['touch_screen']),
                            int(request.args['wifi']),]])
    
    
    
    
    output = round(price_predict[0],0)
    if output == 0:
        mob_pred = 'Rs500 - Rs10,000'
    elif output == 1:
        mob_pred = 'Rs 10,000 - Rs 30,000'
    elif output == 2:
        mob_pred = 'Rs 30,000 - Rs 60,000'
    elif output == 3:
        mob_pred = 'Rs 60,000 - Rs 1,00,000'
    
    return render_template('index1.html',prediction = "Mobile Price Prediction is: {}" .format(output))


# app.run(debug = True)



# app.run(debug = True)

if __name__ == '__main__':
	app.run(debug=True)    
