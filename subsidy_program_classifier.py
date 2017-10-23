import csv
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

df = pd.read_csv('Subsidy_Register.csv')

#make a list of subsidies
subsidies_list =['Basisvoorziening activering', 'Subsidieregeling bewonersinitiatieven', 'Gebiedsgebonden Kunst en cultuuractiviteiten']
subsidies_list = [name.lower() for name in subsidies_list]

def find():
    text = 'Basisvoorziening activering, participatie en sociale accommodaties (SD Zuid)'
    pattern = "basisvoorziening activering"
    text = text.lower()
    #re.search(pattern, text)
    if pattern in text:
        print('Success!')



# subsidies_list = [subsidy.split() for subsidy in subsidies_list]
# print(subsidies_list)
#
# #if column arrangement has the subsidy name, attache target from the list
#
# #set_words = set(subsidies_list.split())
#
# df['Arrangement'] = df['Arrangement'].apply(lambda x: x.split())
#
# df['Arrangement'] = df['Arrangement'].apply(lambda x: [word.lower() for word in x])
# print(df['Arrangement'])

#sklearn requies pandas DataFrame or numpy array
#and no missing values in the data



#Features: Project words to num, Project description length = new column,
#Arrangement (subsidy program), Organization (district), Periodicity (0|1), Requested
#Count the labels from delivered = % of requested
