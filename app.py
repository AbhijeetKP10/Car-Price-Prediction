from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('ran_forest.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        age = int(request.form['age'])
        trestbps=float(request.form['trestbps'])
        chol=int(request.form['chol'])
        thalach=int(request.form['thalach'])
        oldpeak=float(request.form['oldpeak'])
        sex=request.form['sex']
        if(sex=='Male'):
                sex_0 =1
                sex_1 =0
        else:
            sex_0 =0
            sex_1 =1
        cp=request.form['cp']
        if(cp==1):
                cp_0=1
                cp_1=0 
                cp_2=0
                cp_3=0
        elif(cp==2):
                cp_0=0
                cp_1=1 
                cp_2=0
                cp_3=0
        elif(cp==3):
                cp_0=0
                cp_1=0 
                cp_2=1
                cp_3=0
        else:
            cp_0=0
            cp_1=0 
            cp_2=0
            cp_3=1
        fbs=request.form['fbs']
        if(fbs==1):
            fbs_0=1
            fbs_1=0
        else:
            fbs_0=0
            fbs_1=1	
        restecg=request.form['restecg']
        if(restecg==1):
            restecg_0=1
            restecg_1=0
            restecg_2=0
        elif(restecg==1):
            restecg_0=0
            restecg_1=1
            restecg_2=0
        else:
            restecg_0=0
            restecg_1=0
            restecg_2=1
            
        exang=request.form['exang']
        if(exang==1):
            exang_0=1
            exang_1=0
        else:
            exang_0=0
            exang_1=1
        
        slope=request.form['slope']
        if(slope==1):
            slope_0=1
            slope_1=0
            slope_2=0
        elif(slope==1):
            slope_0=0
            slope_1=1
            slope_2=0
        else:
            slope_0=0
            slope_1=0
            slope_2=1
            
        ca=request.form['ca']
        if(ca==1):
                ca_0=1
                ca_1=0 
                ca_2=0
                ca_3=0
                ca_4=0
        elif(ca==2):
                ca_0=0
                ca_1=1 
                ca_2=0
                ca_3=0
                ca_4=0
        elif(ca==3):
                ca_0=0
                ca_1=0 
                ca_2=1
                ca_3=0
                ca_4=0
        elif(ca==4):
                ca_0=0
                ca_1=0 
                ca_2=0
                ca_3=1
                ca_4=0
        else:
            ca_0=0
            ca_1=0 
            ca_2=0
            ca_3=0
            ca_4=1
        
        thal=request.form['thal']
        if(thal==1):
                thal_0=1
                thal_1=0 
                thal_2=0
                thal_3=0
        elif(thal==2):
                thal_0=0
                thal_1=1 
                thal_2=0
                thal_3=0
        elif(thal==3):
                thal_0=0
                thal_1=0 
                thal_2=1
                thal_3=0
        else:
                thal_0=0
                thal_1=0 
                thal_2=0
                thal_3=1
        li=list()
        li=[['Age:',age],['Trestbps:',trestbps],['Chol:',chol],['Thalach:',thalach],['Oldpeak:',oldpeak],['Sex:',sex],['CP:',cp],['FBS:',fbs],['Restecg:',restecg],['Exang:',exang],['Slope:',slope],['CA:',ca],['Thal:',thal]]
        prediction=model.predict([[age, trestbps, chol, thalach, oldpeak,sex_0,sex_1, cp_0, cp_1, cp_2, cp_3, fbs_0, fbs_1, restecg_0,restecg_1, restecg_2, exang_0, exang_1, slope_0, slope_1,slope_2, ca_0, ca_1, ca_2, ca_3, ca_4, thal_0, thal_1,thal_2, thal_3]])
        output=round(prediction[0],2)
        final_list=list()
        if output<0:
            return render_template('index.html',prediction_texts="Sorry Something went wrong with the input values. Please try it again")
        elif output==0:
            return render_template('output.html',prediction_text="You have healthy heart. Keep consuming all the calories which you are taking. Have a healthy heart always",prediction_input=li,input_1="YOUR INPUT: ")
        elif output==1:
            return render_template('output.html',prediction_text="Don't Panic. You have heart which slightly comes under unhealthy category. Please consult to a heart specialist. Keep doing yoga. Hope you will have a healthy heart soon!",prediction_input=li,input_1="YOUR INPUT: ")
        else:
            return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
"""[age, trestbps, chol, thalach, oldpeak,sex_0,sex_1, cp_0, cp_1, cp_2, cp_3, fbs_0, fbs_1, restecg_0,
restecg_1, restecg_2, exang_0, exang_1, slope_0, slope_1,
       slope_2, ca_0, ca_1, ca_2, ca_3, ca_4, thal_0, thal_1,
       thal_2, thal_3]"""
