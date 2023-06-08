# importing pandas package
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
 
# making data frame from csv file
data = pd.read_csv("measurements.csv")
print(data)


x = data['Sunshine hours (hours per day)']
y = data['Billiard club occupancy (%)']



slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show() 

print(slope)

##  y linea_recta

data['y_linea'] = data['Sunshine hours (hours per day)']*slope+ intercept

##  y_real  = ocuppancy

data['diff'] = abs(data['y_linea']-data['Billiard club occupancy (%)'])
print(data)

res = data.sort_values(by='diff')
print(res)


"""
1. 20
2.  12
3.  43

"""
