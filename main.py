# INF601 - Advanced Programming in Python
# Michael Flavin
# Mini Project 2


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from faker import Faker


#Generate Fake Data

fake = Faker();


data = {'NAME': [fake.name(), fake.name(), fake.name(), fake.name(), fake.name(), fake.name()],

        'STATE': [fake.state(), fake.state(), fake.state(), fake.state(), fake.state(), fake.state()],

        'SSN': [fake.ssn(), fake.ssn(), fake.ssn(), fake.ssn(), fake.ssn(), fake.ssn()],

        'MONTH': [fake.month(), fake.month(), fake.month(), fake.month(), fake.month(), fake.month()],

        }


#Plot Data

df = pd.DataFrame(data)

print(df)