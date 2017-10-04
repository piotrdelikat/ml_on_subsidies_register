import pandas as pd

df = pd.read_csv('Subsidy_Register.csv', na_values='€ NaN')
df.drop(['Name', 'Established', 'Year'], axis=1, inplace=True)

subsidies_list = pd.read_csv('subsidies_list.csv', header=None)
subsidies_list = subsidies_list[0].tolist()

#Eur to integers
to_int = ['Requested', 'Delivered']
for column in to_int:
    df[column].fillna(0, inplace=True)
    df[column] = df[column].replace('[\€|\.]', '', regex=True).astype(float)

def specify_subsidy(row):
    global subsidies_list
    subsidies_list = [subsidy.lower() for subsidy in subsidies_list]
    for subsidy in subsidies_list:
        if subsidy in row['Arrangement']:
            return subsidy

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

df['Arrangement'] = df['Arrangement'].apply(str.lower)
df['subsidy'] = df.apply(specify_subsidy, axis=1)
df['description_length'] = df['Project'].apply(len)

print(df.head())
# df.to_csv('cleaned.csv')
