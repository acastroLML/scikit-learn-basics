import numpy as np

from sklearn import linear_model



def desired_marketing_expenditure(marketing_expenditure, units_sold, desired_units_sold):

    """
    :param marketing_expenditure: (list) A list of integers with the expenditure 
        for each previous campaign.
    :param units_sold: (list) A list of integers with the number of units sold 
        for each previous campaign.
    :param desired_units_sold: (integer) Target number of units to sell in the 
        new campaign.
    :returns: (float) Required amount of money to be invested.
    """

    marketing_expenditure = np.asarray(marketing_expenditure).reshape(-1,1)
    units_sold = np.asarray(units_sold).reshape(-1,1)
    model = linear_model.LinearRegression()
    model.fit(marketing_expenditure,units_sold)

    expenditure = (desired_units_sold-model.intercept_)/model.coef_
    
    return expenditure[0][0]



#For example, with the parameters below, the function should return 250000.0

print(desired_marketing_expenditure(
    [300000, 200000, 400000, 300000, 100000],
    [60000, 50000, 90000, 80000, 30000],
    60000))