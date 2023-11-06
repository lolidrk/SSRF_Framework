import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
import joblib

loaded_model = keras.models.load_model('trained_model.h5')
scaler = joblib.load('lstm_scaler.joblib')
    
        
'''
        values = [[4,4.4,4,0.03448276,5,-1,3,0,2,0,3,0.7844933264]]

normalized_input = scaler.transform(values)
values = np.array(normalized_input)
my_array_reshaped = np.expand_dims(values, axis=1)

# Print the reshaped array
print(my_array_reshaped.shape)


predictions = loaded_model.predict(my_array_reshaped)
print(f'PREDICTION FOR LSTM IS {predictions}')
#y_pred = loaded_model.predict(dtest)
#y_pred_binary = (y_pred > 0.5).astype(int
result = 'benign'
'''

def make_prediction(features):
    
    feat = np.array(features)
    featy = feat.reshape(1,-1)
    normalized_input = scaler.transform(featy)
    values = np.array(normalized_input)
    my_array_reshaped = np.expand_dims(values, axis=1)

    # Print the reshaped array
    print(my_array_reshaped.shape)


    predictions = loaded_model.predict(my_array_reshaped)
    print(f'PREDICTION FOR LSTM IS {predictions}')
    y_pred_binary = (predictions > 0.5).astype(int)
    print(f' PREDICTION ISSSSSSSSSSSSSSSSS {y_pred_binary}')
    result = 'malicious' if y_pred_binary == 1 else 'benign'
    return result