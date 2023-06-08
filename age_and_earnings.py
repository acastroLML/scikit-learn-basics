# importing pandas package
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
 
# making data frame from csv file
data = pd.read_csv("earnings_data.csv")
print(data)

x = data['Age']
y = data['Earnings']
plt.scatter(x, y)
plt.show()


slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show() 

print(slope)


"""
answer = 1467
"""
