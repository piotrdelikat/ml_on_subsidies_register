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


def handle_non_numerical_data(df):
    to_numeric = ['Organization', 'Theme', 'Periodicity']
    for column in to_numeric:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]

        column_contents = df[column].values.tolist()
        unique_elements = set(column_contents)
        x = 0
        for unique in unique_elements:
            if unique not in text_digit_vals:
                text_digit_vals[unique] = x
                x+=1
        df[column] = list(map(convert_to_int, df[column]))
    return df

df = handle_non_numerical_data(df)
print(df.head())

#Features: list Name [0|1], Project words to num, Project description length = new column,
# Arrangement (subsidy program), Organization (district), Periodicity (0|1), Requested

#Count the labels from delivered = % of requested
#Normalize target

