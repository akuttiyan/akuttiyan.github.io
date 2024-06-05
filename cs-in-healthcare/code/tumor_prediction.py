# Arya Kuttiyan
# Computer Science in Healthcare
# May 10 2024
# This program looks at data on tumors and classifies which ones are bengin and malignant

# Used for classifications
from sklearn.model_selection import KFold, train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier

import csv

# Opens breast cancer tumor data file
breast_cancer_data = open("breast-cancer.csv")

# reads the data into the csv reader
csv_reader = csv.reader(breast_cancer_data)

data = []
targets = []

# Puts the tumor characteristic data in the csv reader into a list
# Puts the labels (benign or malignant) in the targets list
for row in csv_reader:
    data.append(row[2 : 32])
    targets.append(row[1])

# Converts the tumor characteristic list into a list of floats instead of a list of strings
float_data = []
sub_list = []
i = 0
# Loops through each row in the tumor characteristics list
for row in data[1 : 570]:
    # Loops through each data point in the row
    for data_point in row:

        # Converts each data point from a string to a float
        # Adds the floats to a sublist
        sub_list.append(float(data_point))
    # Adds the sublist to a float list of the data
    float_data.append(sub_list[i : i + 30])
    i += 30

# Splits the data and targets into testing data and training data
x_train, x_test, y_train, y_test = train_test_split(float_data, targets[1: 570], random_state=11)

# Create the K Neighbors Classifer to make predictions
knn = KNeighborsClassifier()

# Fits the model to the training data
knn.fit(X=x_train, y=y_train)

# Makes predictions on the testing data to predict if the tumor is benign or malignant
predict = knn.predict(X=x_test)

# These are the actual labels of the testing data
expect = y_test

# prints the first 20 predicted values for the tumors
print("predicted", predict[:20])

# prints the first 20 expected values for the tumors
print("expected", expect[:20])

# Prints a score on how accurate the predictions were
print(f'{knn.score(x_test, y_test)}')

# closes the file
breast_cancer_data.close()
