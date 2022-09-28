# INF601 - Advanced Programming in Python
# Michael Flavin
# Mini Project 2


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

stats_2017 = {
        'Rebounds': [3, 1, 4, 2, 2, 3],

        'Points': [13, 25, 16, 7, 19, 13],

        'Assists': [2, 0, 0, 4, 1, 3],

        'Blocks': [3, 1, 3, 5, 0, 1],

        'Fouls': [4, 2, 1, 2, 4, 4]
}


stats_2018 = {
        'Rebounds': [5, 6, 2, 4, 5, 5],

        'Points': [23, 25, 26, 21, 29, 23],

        'Assists': [4, 5, 2, 4, 3, 6],

        'Blocks': [4, 5, 6, 5, 3, 2],

        'Fouls': [3, 5, 4, 2, 1, 1]
}

stats_2019 = {
        'Rebounds': [8, 5, 5, 3, 1, 5],

        'Points': [24, 32, 17, 15, 26, 21],

        'Assists': [4, 3, 5, 4, 1, 3],

        'Blocks': [3, 1, 3, 5, 0, 1],

        'Fouls': [4, 2, 1, 2, 4, 4]
}



stats_2020 = {
        'Rebounds': [4, 6, 8, 7, 3, 6],

        'Points': [23, 35, 31, 28, 26, 33],

        'Assists': [6, 4, 4, 1, 3, 4],

        'Blocks': [4, 1, 2, 2, 3, 5],

        'Fouls': [2, 3, 4, 4, 1, 2]
}


stats_2021 = {
        'Rebounds': [5, 4, 6, 12, 4, 6],

        'Points': [41, 36, 29, 19, 39, 37],

        'Assists': [4, 2, 6, 4, 1, 0],

        'Blocks': [2, 0, 0, 4, 3, 2],

        'Fouls': [2, 3, 1, 5, 3, 4]
}


def process_stats(stats_data, stats_png_name):

        #Put dictionary data into dataframe

        df = pd.DataFrame(stats_data)
        print(df)

        # Create the NumPy Array

        numpy_array = np.array(df)


        # Create the MatLib graph

        plt.plot(numpy_array)

        # Save graph to charts folder

        plt.savefig('charts/' + stats_png_name + '.png')

        plt.show()



process_stats(stats_2017, "stats2017")

process_stats(stats_2018, "stats2018")

process_stats(stats_2019, "stats2019")

process_stats(stats_2020, "stats2020")

process_stats(stats_2021, "stats2021")