import sys
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

df = pd.read_csv('cleaned.csv')

X = df['Project'].values
y = df['Subsidy'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=21, stratify=y)

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', KNeighborsClassifier(n_neighbors=3)),
])

text_clf = text_clf.fit(X_train, y_train)

predicted = text_clf.predict(X_test)
print(text_clf.score(X_test, y_test))

predict = sys.argv[1]
prediction = text_clf.predict(predict)

#change number to subsidy name
for row in df[['Subsidy']].itertuples():
    if row[1] == prediction:
        print(df.iloc[row[0], 9])
        break