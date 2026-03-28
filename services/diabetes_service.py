import pickle
import numpy as np
from schemas.diabetes_schema import PatientDiabetesData


with open('RFDiabetesv132.pkl','rb') as file:
    RF_model2 = pickle.load(file)

labels = ['Sano', 'Diabetes']



def diabetes_prediction(data: PatientDiabetesData):

    xin = np.array([

        data.pregnancies,
        data.glucose,
        data.bloodpressure,
        data.skinthickness,
        data.insulin,
        data.bmi,
        data.diabetespedigreefunction,
        data.age
    ]).reshape(1,8)

    prediction = RF_model2.predict(xin)
    
    print("xin shape:", xin.shape)
    print(labels[prediction[0]])
    return labels[prediction[0]]