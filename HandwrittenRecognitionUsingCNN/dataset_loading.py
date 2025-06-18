import pandas as pd
from sklearn.utils import shuffle

# Shuffling of Data
data = pd.read_csv('Dataset.csv')
data = shuffle(data)
# print(data)

# Separation of Dependent and Independent Variable
X_Axis = data.drop(["Lable"], axis = 1)
Y_Axis = data["Lable"]
