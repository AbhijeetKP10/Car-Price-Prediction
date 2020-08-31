from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Year_1 = int(request.form['Year'])
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        Kms_Driven2=np.log(Kms_Driven)
        Owner=int(request.form['Owner'])
        Fuel_Type=request.form['Fuel_Type_Petrol']
        if(Fuel_Type=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
        elif(Fuel_Type=='Diesel'):
                Fuel_Type_Petrol=0
                Fuel_Type_Diesel=1
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
        Year=2020-Year_1
        Seller_Type=request.form['Seller_Type_Individual']
        if(Seller_Type=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0	
        Transmission=request.form['Transmission_Mannual']
        if(Transmission=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0
        prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
        output=round(prediction[0],2)
        li=list()
        li=[['Year: ',Year_1],['Present Price: ',Present_Price],['Kilometers Driven: ',Kms_Driven],['Number of Owner: ',Owner],['Fuel Type: ',Fuel_Type],['Seller Type: ',Seller_Type],['Transmission Type: ',Transmission]]
        if Year>=0:            
            if output<0:
                return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
            else:
                return render_template('output.html',prediction_text="You Can Sell The Car at {}".format(output),inp=li)
        else:
            return render_template('index.html',prediction_texts="You can not predict future bought car selling price.Try with past bought car.")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

