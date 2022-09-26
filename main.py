# INF601 - Advanced Programming in Python
# Michael Flavin
# Mini Project 2


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from faker import Faker

fake = Faker();

# Generate Fake Data

for _ in range(5):
    print(fake.simple_profile())





df = pd.DataFrame(

    {

        "Name": [

            "Braund, Mr. Owen Harris",

            "Allen, Mr. William Henry",

            "Bonnell, Miss. Elizabeth",

        ],

        "Age": [22, 35, 58],

        "Sex": ["male", "male", "female"],

    }

)

print(df)