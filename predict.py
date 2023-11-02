import xgboost as xgb
import pandas as pd

loaded_model = xgb.Booster(model_file='xgboost_model.model')
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

dtest = xgb.DMatrix(input_data)
y_pred = loaded_model.predict(dtest)
print(y_pred)