# importing pandas package
import pandas as pd
 
# making data frame from csv file
data = pd.read_csv("data_wq.csv")
print(data)

correlacion = data.corr()
print(correlacion)

"""
answer collinearity

- sweetness
- body
- Price
"""