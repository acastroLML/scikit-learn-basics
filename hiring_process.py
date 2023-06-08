# importing pandas package
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.tree import DecisionTreeClassifier
 
# making data frame from csv file
data = pd.read_csv("hiring_data.csv")
print(data)
print(len(data))

data_5_years = data[data['Years of experience?']>=5]
data_5_years = data_5_years.reset_index()
print(data_5_years)
print(len(data_5_years))

data_5_year_hiring = data_5_years[data_5_years['Passed hiring process?']=='Yes']
print("fueron contratados" ,len(data_5_year_hiring))


data_previo = data[data['Manager at previous position?']=='Yes']
print(len(data_previo))

data_previo_hiring = data_previo[data_previo['Passed hiring process?']=='Yes']
print("fueron contratados previo" ,len(data_previo_hiring))

"""
respuesta accuracy 87%
"""


data_fail = data[(data['Manager at previous position?']=='No') & (data['Passed hiring process?']=='No')]
print("data_fail ", len(data_fail))

data_fail_hiring = data_fail[data_fail['Passed hiring process?']=='Yes']
print("fueron contratados previo" ,len(data_fail_hiring))


