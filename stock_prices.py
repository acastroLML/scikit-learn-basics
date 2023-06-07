import pandas as pd
import numpy as np

def factorial(num):
    if num <0:
        pass
    elif num==0:
        return 1
    else:
        fact = 1
        while (num > 1):
            fact *= num
            num-=1
        return fact
    
def most_corr(prices):
    """

    :param prices: (pandas.DataFrame) A dataframe containing each ticker's 

                   daily closing prices.

    :returns: (container of strings) A container, containing the two tickers that 

              are the most highly (linearly) correlated by daily percentage change.

    """
    prices = pd.DataFrame(prices)   
    cor = prices.pct_change().corr().unstack() # correlation of % change for each pair of stocks
    cor = cor[cor != 1].sort_values(ascending=False, kind='quicksort') # take out field with value = 1, and sort by values
    return list(cor.index[0]) # return the most correlated pair of stocks



def corr_columns(prices):
    tickers = list(prices.columns)
    print(tickers)

    num_tickers= len(tickers)
    print("there are: ", num_tickers, "tickers")
    permutaciones = factorial(num_tickers-1)
    print(permutaciones)

    matriz_corr = prices.corr()
    print(matriz_corr)

    percentual_change_df = prices.pct_change()
    eliminando_nulos = percentual_change_df.dropna()
    print("percentual change df ", percentual_change_df)
    print("eliminando nulos ", eliminando_nulos)

    matriz_corr_perc_change = eliminando_nulos.corr()
    print(matriz_corr_perc_change)

    unstack_matrix = matriz_corr_perc_change.unstack()
    print(unstack_matrix)






#For example, the code below should print: ('FB', 'MSFT')

print(most_corr(pd.DataFrame.from_dict({

    'GOOG' : [

        742.66, 738.40, 738.22, 741.16,

        739.98, 747.28, 746.22, 741.80,

        745.33, 741.29, 742.83, 750.50

    ],

    'FB' : [

        108.40, 107.92, 109.64, 112.22,

        109.57, 113.82, 114.03, 112.24,

        114.68, 112.92, 113.28, 115.40

    ],

    'MSFT' : [

        55.40, 54.63, 54.98, 55.88,

        54.12, 59.16, 58.14, 55.97,

        61.20, 57.14, 56.62, 59.25

    ],

    'AAPL' : [

        106.00, 104.66, 104.87, 105.69,

        104.22, 110.16, 109.84, 108.86,

        110.14, 107.66, 108.08, 109.90

    ]

})))




example_df = pd.DataFrame.from_dict({

    'GOOG' : [

        742.66, 738.40, 738.22, 741.16,

        739.98, 747.28, 746.22, 741.80,

        745.33, 741.29, 742.83, 750.50

    ],

    'FB' : [

        108.40, 107.92, 109.64, 112.22,

        109.57, 113.82, 114.03, 112.24,

        114.68, 112.92, 113.28, 115.40

    ],

    'MSFT' : [

        55.40, 54.63, 54.98, 55.88,

        54.12, 59.16, 58.14, 55.97,

        61.20, 57.14, 56.62, 59.25

    ],

    'AAPL' : [

        106.00, 104.66, 104.87, 105.69,

        104.22, 110.16, 109.84, 108.86,

        110.14, 107.66, 108.08, 109.90

    ]

})

print(example_df)

print(corr_columns(example_df))

