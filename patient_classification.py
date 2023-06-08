# importing pandas package
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import confusion_matrix
 
# making data frame from csv file
data = pd.read_csv("patient_class.csv")
print(data)


y_test=data['Patient needed procedure']


y_pred_porc= data['Classificator prediction']

threshold = 59
data['y_pred'] = data['Classificator prediction'].gt(threshold).astype(bool)
print(data)

y_pred= data['y_pred']

"""
respuesta 59
"""


print(confusion_matrix(y_test, y_pred))
