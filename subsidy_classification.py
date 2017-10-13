import sys
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

df = pd.read_csv('cleaned.csv')

X = df['Project'].values
y = df['subsidy'].values

count_vect = CountVectorizer()
tfidf_transformer = TfidfTransformer()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42, stratify=y)

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB()),
])

text_clf = text_clf.fit(X_train, y_train)

predicted = text_clf.predict(X_test)
print(np.mean(predicted == y_test))

predict = sys.argv[1]
predicted_subsidy = text_clf.predict(predict)
print(predicted_subsidy)

#changeing number to subsidy name