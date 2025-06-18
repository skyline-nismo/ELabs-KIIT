import dataset_loading as dl

# Training and Testing split
from sklearn.model_selection import train_test_split

train_X, test_X, train_Y, test_Y = train_test_split(dl.X_Axis, dl.Y_Axis, test_size= 0.2)
'''
Here 20% of images are used for testing purpose and 80% of images are used for training purpose.

Training images are used to create model and Testsing images are used for calculating accuracy.
'''

# Fitting the model using 'SVC' and then save the model using 'joblib'
from sklearn.svm import SVC
import joblib

classifier = SVC(kernel= "linear", random_state= 6)
classifier.fit(train_X, train_Y)
joblib.dump(classifier, "model/digit_recognizer")

from sklearn import metrics

prediction = classifier.predict(test_X)
print("Accuracy = ", metrics.accuracy_score(prediction, test_Y) * 100, end="%")