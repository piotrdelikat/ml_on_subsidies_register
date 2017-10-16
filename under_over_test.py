import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

df = pd.read_csv('cleaned.csv')

neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

X = df['Project'].values
y = df['Subsidy'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=21, stratify=y)

# Loop over different values of k
for i, k in enumerate(neighbors):
    # Setup a k-NN Classifier pipeline with k neighbors: knn
    text_clf = Pipeline([('vect', CountVectorizer()),
                         ('tfidf', TfidfTransformer()),
                         ('clf', KNeighborsClassifier(n_neighbors=k)),
                         ])

    # Fit the classifier to the training data
    text_clf = text_clf.fit(X_train, y_train)

    # Compute accuracy on the training set
    train_accuracy[i] = text_clf.score(X_train, y_train)

    # Compute accuracy on the testing set
    test_accuracy[i] = text_clf.score(X_test, y_test)

plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label = 'Testing Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()

