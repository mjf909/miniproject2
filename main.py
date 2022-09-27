# INF601 - Advanced Programming in Python
# Michael Flavin
# Mini Project 2


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json




data = {
        'Rebounds': [3, 1, 4, 2, 2, 3],

        'Points': [13, 25, 16, 7, 19, 13],

        'Assists': [2, 0, 0, 4, 1, 3],

        'Blocks': [3, 1, 3, 5, 0, 1],

        'Fouls': [4, 2, 1, 2, 4, 4],
}

df = pd.DataFrame(data)

print(df)


# Create the NumPy Array

ticker_array = np.array(df)


# Create the MatLib graph

plt.plot(ticker_array)


plt.show()