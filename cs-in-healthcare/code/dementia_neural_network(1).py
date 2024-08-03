# Arya Kuttiyan
# Computer Science in Healthcare
# 5/28/24
# The purpose of this code is to use a neural network to predict if someone
# is more likely to have dementia based on genetic risk and their lifestyle

# Code from real python.com
import numpy as np
from keras import Sequential
from keras.layers import Dense, BatchNormalization
from sklearn.model_selection import train_test_split
import csv

# Opens data file
dementia_data = open("dementia_patient_data.csv")

# Reads the file with csv
csv_reader = csv.reader(dementia_data)

######################## Tweaking the Model #####################################
'''
############ First I used all the data in the data file and put all the data in the neural network ##########
data = []
targets = []

# Loops through all the rows in the csv reader
for row in csv_reader:
    # Appends all the features to one list
    data.append(row[0 : 21])
    # Appends all the targets to another list
    targets.append(row[21])

float_data = []
sub_list = []
target_sublist = []
target_floats = []
i = 0
j = 0
# Loops through each row
for row in data[1 : 1002]:
    # Loops through each data point in the row
    for data_point in row:
        # Converts each data point from a string to a float
        # Adds the floats to a sublist
        sub_list.append(float(data_point))
    # Adds the sublist to a float list of the data
    float_data.append(sub_list[i : i + 21])
    i += 21

# Loops through each row in the targets list
for target_row in targets[1 : 1002]:
    # Loops through each data point in the row
    for target_data_point in target_row:
        # Converts each data point from a string to a float
        # Adds the floats to a sublist
        target_floats.append(float(target_data_point))

# Does a train test split
# Takes a portion of data and uses it for training the model
# The other part of the data is for testing the model
x_train, x_test, y_train, y_test = train_test_split(float_data, target_floats, random_state=11)


####3 Code from Sebastiaan Mathot

# Sequential neural network
model = Sequential(
    [
        # There are 2 dense layers
        # The input shape is 21 because that is the length of the list that I input into the model
        Dense(units=8, input_shape=(21,), activation="relu"), # 8 nodes with relu activation function

        Dense(units=2, activation="softmax") # 2 nodes with softmax activation function
    ]
)

# Added another layer
model = Sequential(
    [
        # 3 Dense layers
        Dense(units=8, input_shape=(21,), activation="relu"), # 8 nodes with relu activation function
        Dense(units=2, activation="relu"), # 2 nodes with relu activation function
        Dense(units=2, activation="softmax"), # 2 nodes with softmax activations function

    ]
)

# Added another layer
# Changed the number of nodes in each layer
model = Sequential(
    [
        Dense(units=20, input_shape=(21,), activation="relu"), # 20 nodes rule activation function
        Dense(units=16, activation="relu"), # 16 nodes rule activation function
        Dense(units=8, activation="relu"), # 8 nodes relu activation function
        Dense(units=2, activation="softmax") # 2 nodes softmax activation fuction

    ]
)

# Changed activation functions
model = Sequential(
    [
        # Activation functions are tanh for all the layers
        Dense(units=20, input_shape=(21,), activation="tanh"), 
        Dense(units=16, activation="tanh"),
        Dense(units=8, activation="tanh"),
        Dense(units=2, activation="tanh")


    ]
)

# Used this model for the final model
# Changed activation functions again
model = Sequential(
    [
        Dense(units=20, input_shape=(21,), activation="sigmoid"),
        Dense(units=16, activation="sigmoid"),
        Dense(units=8, activation="sigmoid"),
        Dense(units=2, activation="softmax")
    ]
)

# Prints summary of the model
# Prints layer types and shapes
print(model.summary())

# compiles the model
model.compile(
    loss="sparse_categorical_crossentropy", # loss function finds the errors in the predictions
    optimizer="adam", # Optimizer minimizes loss
    metrics= ["accuracy"] # Prints the accuracy
)

# Fits the model to the training data
model.fit(
    x=np.array(x_train),
    y=np.array(y_train),
    epochs=10, # Runs the model through the training data 10 times
    verbose=2,
    
)
# Training Model Accuracy: 52.13%

# Makes predictions using the testing data
predictions = model.predict(x_test)

# Expected values
expected = y_test

# np.argmax decodes the predictions
# The predictions are a 2d list
# Each sublist has 2 numbers
# The argmax function finds which of these 2 numbers is larger and print its index
# The index is either 0 or 1 and this tells us what the prediction is
other_predictions = np.argmax(predictions, axis=1)

num_correct = 0
total = 0

# Loops through the decoded predictions and te expected vales
for i in range(len(other_predictions)):
    # If the prediction is correct
    if int(expected[i]) == other_predictions[i]:
        # Add 1 to the number of correct predictions
        num_correct += 1
    # Add 1 to the total no matter what
    total += 1

# Finds the accuracy score by dividing the num correct by the total
accuracy_score = num_correct/total

print(accuracy_score) # Accuracy Score = 0.512
'''
############ Here I decided to put only the top 5 features I found to be most #####################
############ impactful from the dementia data analysis file in the neural network ##############

data = []
targets = []

# Loops through every row in the csv reader
for row in csv_reader:
    # Only adds the top 5 most impactful features to the data list
    # Also adds the targets to a targets list
    data.append([row[8], row[13], row[14], row[20], row[9]]) 
    targets.append(row[21])


sub_list = []
float_data = []
target_floats = []
i = 0

# Loops through each row in the data list
for row in data[1 : 1002]:
    # Loops through each data point in the row
    for data_point in row:
        # Converts each data point from a string to a float
        # Adds the floats to a sublist
        sub_list.append(float(data_point))
    # Adds the sublist to a float list of the data
    float_data.append(sub_list[i : i + 5])
    i += 5

# Loops through each row in the targets list
for target_row in targets[1 : 1002]:
    # Loops through each data point in the row
    for target_data_point in target_row:
        # Converts each data point from a string to a float
        # Adds the floats to a sublist
        target_floats.append(float(target_data_point))


# Does a train test split
# Takes a portion of data and uses it for training the model
# The other part of the data is for testing the model
x_train, x_test, y_train, y_test = train_test_split(float_data, target_floats, random_state=11)

# Sets up neural network
model = Sequential(
    [
        # Uses 4 Dense layers
        # Input shape is 5 because the lenth of the list we are inputting is 5
        Dense(units=20, input_shape=(5,), activation="sigmoid"), # 20 nodes and sigmoid activation function
        Dense(units=16, activation="sigmoid"), # 16 nodes and sigmoid activation function
        Dense(units=8, activation="sigmoid"), # 8 nodes and sigmoid activation function
        Dense(units=2, activation="softmax") # 2 nodes and softmax activation function
    ]
)

# Prints the summary of the model
# Layer types, shape etc.
print(model.summary())

# Complies the model
model.compile(
    loss="sparse_categorical_crossentropy", # Loss finds the errors in the predictions
    optimizer="adam", # Optimizer minimizes the loss
    metrics= ["accuracy"] # Prints the accuracy
)

# Fits the model to the training data
model.fit(
    x=np.array(x_train),
    y=np.array(y_train),
    epochs=10, # Runs the model with the training data 10 times
    verbose=2,
    
)
# Model Accuracy = 88%

# Makes predictions using the testing data
predictions = model.predict(x_test)

# Expected values
expected = y_test

# np.argmax decodes the predictions
# The predictions are a 2d list
# Each sublist has 2 numbers
# The argmax function finds which of these 2 numbers is larger and print its index
# The index is either 0 or 1 and this tells us what the prediction is
other_predictions = np.argmax(predictions, axis=1)

num_correct = 0
total = 0

# Loops through the decoded predictions and te expected vales
for i in range(len(other_predictions)):
    # If the prediction is correct
    if int(expected[i]) == other_predictions[i]:
        # Add 1 to the number of correct predictions
        num_correct += 1
    # Add 1 to the total no matter what
    total += 1

# Finds the accuracy score by dividing the num correct by the total
accuracy_score = num_correct/total

print(accuracy_score) # Accuracy score = 90%
