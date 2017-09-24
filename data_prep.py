import pandas as pd

df = pd.read_csv('Subsidy_Register.csv')

print(df.head())

#Cleaning
#Eur to integers




#Features: list Name [0|1], Project words (is words tokenization nesscessary?), Project lenght,
# Arrangement (subsidy program), Organization (district), Periodicity (0|1), Requested

#Count the labels from delivered = % of requested
#Normalize target

