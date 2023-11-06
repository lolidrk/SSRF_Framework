import xgboost as xgb
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

loaded_model = xgb.Booster(model_file='xgboost_model.model')
scaler = joblib.load('scaler.pkl')
'''              
#data needs to be normalized tho
input_data= pd.DataFrame({
    'domain_token_count': [4], 
    'avgpathtokenlen': [4.4], 
    'tld' : [4], 
    'ArgUrlRatio' : [0.03448276],
    'NumberofDotsinURL': [5], 
    'Arguments_LongestWordLength' : [-1], 
    'spcharUrl': [3],
    'delimeter_Domain': [0], 
    'delimeter_path':[2], 
    'NumberRate_DirectoryName': [0],
    'SymbolCount_Domain': [3], 
    'Entropy_Domain': [0.7844933264]
})

nomalized_input = scaler.transform(input_data)
dtest = xgb.DMatrix(nomalized_input)
y_pred = loaded_model.predict(dtest)
y_pred_binary = (y_pred > 0.5).astype(int)
print(y_pred)
print(y_pred_binary)
'''

def make_prediction(features):
    input_data = pd.DataFrame({
        'domain_token_count': features[0],
        'avgpathtokenlen': features[1],
        'tld': features[2],
        'ArgUrlRatio': features[3],
        'NumberofDotsinURL': features[4],
        'Arguments_LongestWordLength': features[5],
        'spcharUrl': features[6],
        'delimeter_Domain': features[7],
        'delimeter_path': features[8],
        'NumberRate_DirectoryName': features[9],
        'SymbolCount_Domain': features[10],
        'Entropy_Domain': features[11]
    })
    
    normalized_input = scaler.transform(features)
    dtest = xgb.DMatrix(normalized_input)
    y_pred = loaded_model.predict(dtest)
    print(f' Y PRED ISS {y_pred}')
    y_pred_binary = (y_pred > 0.5).astype(int)
    print(f' PREDICTION ISSSSSSSSSSSSSSSSS {y_pred_binary}')
    result = 'malicious' if y_pred_binary == 1 else 'benign'

    return result

