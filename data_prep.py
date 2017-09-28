import pandas as pd
import numpy as np

df = pd.read_csv('Subsidy_Register.csv', na_values='€ NaN')
df.drop(['Established', 'Year'], axis=1, inplace=True)

#Cleaning

#Eur to integers
to_int = ['Requested', 'Delivered']
for column in to_int:
    df[column].fillna(0, inplace=True)
    df[column] = df[column].replace('[\€|\.]', '', regex=True).astype(float)

print(df.info())

#Features: list Name [0|1], Project words (is words tokenization nesscessary?), Project description length,
# Arrangement (subsidy program), Organization (district), Periodicity (0|1), Requested

#Count the labels from delivered = % of requested
#Normalize target

