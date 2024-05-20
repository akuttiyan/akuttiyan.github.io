# Arya Kuttiyan
# Advanced Programming Topics in Computer Science
# March 8 2024
# Uses kmeans to predict how at risk trees in a sklearn dataset are

# The dataset
from sklearn.datasets import fetch_covtype

from sklearn.model_selection import KFold, train_test_split, cross_val_score 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix, classification_report,silhouette_score

# Data vizualiation
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import csv

import math

patient_data = open("cancer_patient_data.csv")
csv_reader = csv.reader(patient_data)

rows = [] 
# Adds all the rows in the file to a list
for row in csv_reader: # From Analytics Vidhya
    rows.append(row) # From Analytics Vidhya

print(rows)

''''''
'''
The purpose of this function is to turns the coordinates of each centroid into
a 2d list. Ex: [[x_1, y_1, z_1], [x_2, y_2, z_2], [x_3, y_3, z_3]]

Parameters: A list of the coordinates of the centroids, it is in the 
this form: [[x_1 y_1 z_1], [x_2 y_2 z_2]]

It also takes the dimensions of the graph. These centroids have x, y, and z
coordinates, so I would input 3 dimensions.

Returns: A 2d list with sublists of the x, y, and z coordinates of a centroid
'''
def prepare_center(centers, dimensions):
    # Initalize the list of centers
    center_list = []
    # Initalizes the sublist
    sublist = []
    i = 0
    # Looks at every centroid in the centroid list
    for center in centers:
        # Looks at every coordinate for the centroid (x, y, z)
        for point in center:
            # Appends the coordinate to a sublist
            sublist.append(point)
        # the sublist now has the x, y, and z coordinate of the center
        # appends the sublist of these coordinates to a bigger list
        center_list.append(sublist[i:i + dimensions])
        # Increments i by the amount that the loop needs
        # to cycle through the rest of the centroids
        i += dimensions

    # returns the list of the centroids
    return center_list

'''
The purpose of this function is to find the centroid that is the closest to
a given point.
It uses the distance formula to find the distance between the centroids and
the point, 
and returns the center with the minimum distance

Parameters: A 2d list of the centroid's coordinates and a list with the 
coordinates of a point, ex. [x, y, z]

Returns: The center that is closest to the point
'''
def get_closest_centroid(centroid_list, point):
    # Initializes the min_distance to infinity
    min_distance = math.inf
    closest_center = []
    sum_distance = 0
    # Looks at every center in the center list
    for center in centroid_list:
        sum_distance = 0
        # Looks at every coordinate variable in the center and the given point
        for j in range(len(point)):
            # Begins computing the distance formula
            sum_distance += (point[j] - center[j]) ** 2
        # Completes the distance formula by taking the square root of the sum
        distance = math.sqrt(sum_distance)
        # This checks to find the centroid that the test data point is
        # closest to
        if distance < min_distance:
            # If the distance is less then the previous minimum distance,
            # then that distance becomes
            # the new min distance
            min_distance = distance
            # Everytime a new minimum distance is found, 
            # the center is appended to a list
            # So the last element in the list is the center that
            #  the point is closest to
            closest_center.append(center)

    # returns the last element in the closest center list
    return closest_center[len(closest_center) - 1]   

# This gets the tree cover data
cover_type = fetch_covtype()

# Prints a description about the data
print(cover_type.DESCR)

# This samples the data
# It takes a target label every 10 target labels, and stores it in a new list
sample_cover_type = cover_type.target[0::10]
# This takes a datapoint every 10 datapoints and stores it in a new list
sample_data = cover_type.data[0::10]

# This is a Pandas dataFrame of all the features in the data
cover_df = pd.DataFrame(sample_data, columns=cover_type.feature_names)
# This takes 10 percent of the data
sample_cover_df = cover_df.sample(frac=0.1, random_state=17)

# This splits the cover_df data frame into a training data 
# frame to train the kmeans model
# It also only takes 3 features: Horizontal_Distance_To_Fire_Points, 
# Horizontal_Distance_To_Hydrology and Horizontal_Distance_To_Roadways
# It only takes the first 4648 datapoints of each feature for the training
train_danger_df = pd.DataFrame(sample_cover_df["Horizontal_Distance_To_Fire_Points"].iloc[0:4649],
                                columns=["Horizontal_Distance_To_Fire_Points"])
train_danger_df["Horizontal_Distance_To_Hydrology"] = sample_cover_df.Horizontal_Distance_To_Hydrology.iloc[0:4649]
train_danger_df["Horizontal_Distance_To_Roadways"] = sample_cover_df.Horizontal_Distance_To_Roadways.iloc[0:4649]

# This takes the remaining datapoints from the 3 features and puts them
# into a testing dataframe to test the kmeans model to make predictions
test_danger_df = pd.DataFrame(sample_cover_df["Horizontal_Distance_To_Fire_Points"].iloc[4649: 5811])
test_danger_df["Horizontal_Distance_To_Hydrology"] = sample_cover_df.Horizontal_Distance_To_Hydrology.iloc[4649: 5811]
test_danger_df["Horizontal_Distance_To_Roadways"] = sample_cover_df.Horizontal_Distance_To_Roadways.iloc[4649:5811]

# Initalizes list of the data
danger_data = []
# Initalizes the sublists
sublist = []
j = 0
# This for loop prepares the training dataframe for kmeans
# It makes the data into a 2d list with each sublist representing each datapoint
# The sublists are in the form: [[x_1, y_1, z_1], [x_2, y_2, z_2]], where x
# is the horizontal distance to fire points, y is the horizontal distance to 
# hydrology and z is the horizontal distance to roadways
# Looks at every data point
for i in range(len(list(train_danger_df["Horizontal_Distance_To_Fire_Points"]))):
    # Appends the horizontal distance to fire points to a sublist
    sublist.append(list(train_danger_df["Horizontal_Distance_To_Fire_Points"])[i])
    # Appends the horizontal distance to hydrology to a sublist
    sublist.append(list(train_danger_df["Horizontal_Distance_To_Hydrology"])[i])
    # Appends the horizontal distance to roadways to a sublist
    sublist.append(list(train_danger_df["Horizontal_Distance_To_Roadways"])[i])
    # adds the sublist a larger list
    danger_data.append(sublist[j:j + 3])
    j += 3

# Code lines 155-172 are from Scaler.com
# This sets up the figure
fig = plt.figure() 
# This sets of the 3d graph
ax = fig.add_subplot(projection='3d')
# Assigns the data to their corresponding variables
x = train_danger_df["Horizontal_Distance_To_Fire_Points"]
y = train_danger_df["Horizontal_Distance_To_Hydrology"]
z = train_danger_df["Horizontal_Distance_To_Roadways"]

# Plots the training datapoints on a scatter plot
ax.scatter(x, y, z, c='r', marker='o', s=1)

# Adds labels to the axes
ax.set_xlabel('Distance from Fire Points')
ax.set_ylabel('Distance From Water')
ax.set_zlabel('Distance From Roadways')

# Shows the graph
plt.show()

'''
# This is my first iteration of the model

# Initalizes list of the data
danger_data = []
# Initalizes the sublists
sublist = []
j = 0
# This for loop prepares the training dataframe for kmeans
# It makes the data into a 2d list with each sublist representing each datapoint
# the sublists are in the form: [[x_1, y_1], [x_2, y_2]], where x
# is the horizontal distance to fire points, y is the horizontal distance to 
# hydrology
# Looks at every data point
for i in range(len(list(train_danger_df["Horizontal_Distance_To_Fire_Points"]))):
    # Appends the horizontal distance to fire points to a sublist
    sublist.append(list(train_danger_df["Horizontal_Distance_To_Fire_Points"])[i])
    # Appends the horizontal distance to hydrology to a sublist
    sublist.append(list(train_danger_df["Horizontal_Distance_To_Hydrology"])[i])
    # adds the sublist a larger list
    danger_data.append(sublist[j:j + 2])
    j += 2

# This sets up the kmeans model with 3 clusters
# The kmeans model looks at all the datapoints and randomly 
# puts in the centroids on the graph
# It then reassigns the centroids to positions that are the average of the
# points
# closest to the centroids
# This process repeats until the centroids don't change their position 
# very much
kmeans = KMeans(n_clusters=3, random_state=11)

# This fits the kmeans model to the training data
kmeans.fit(danger_data)

# This plots the data on 2 dimensions
# I used horizontal distance to fire points for x,
# and horizontal distance to hydrology for y
axes = sns.scatterplot(data=train_danger_df,
                        x='Horizontal_Distance_To_Fire_Points',
                        y='Horizontal_Distance_To_Hydrology', legend='brief')

# This gets the coordinates of the clusters
centroids = kmeans.cluster_centers_
# This prepares the centroids to be plotted
centers = prepare_center(centroids, 2)

# This plots the centroids
for i in range(len(centers)):
    axes.scatter(centers[i][0], centers[i][1], s=100, c='k')

plt.show()

# This gets the predictions for the testing data
# It looks at every testing datapoit
for i in range(1161):
    points = []
    # Gets the x value of a datapoint
    x_1 = list(test_danger_df["Horizontal_Distance_To_Fire_Points"])[i]
    # Gets the y value of a datapoint
    y_1 = list(test_danger_df["Horizontal_Distance_To_Hydrology"])[i]

    # Appends the x and y value to a list
    points.append(x_1)
    points.append(y_1)

    # Finds the closest centroid to the given point
    closest_centroid = get_closest_centroid(centers, points)

    # This determines how at risk the tree it
    # if the point is closest to the first centroid in the list
    if closest_centroid == centers[0]:
        # then that test datapoint is at moderate risk
        print("point" , x_1, ",", y_1,"moderate risk" )
    # If the test data point is closest to the second centroid in the list
    elif closest_centroid == centers[1]:
        # then the test data point is at a lower risk
        print("point" , x_1, ",",y_1, "is lower risk")
    # If the test data point is closest to the third centroid in the list
    elif closest_centroid == centers[2]:
        # then the test data point is at a higher risk
        print("point" , x_1, ",",y_1, "is higher risk")
'''

# This sets up the Kmeans model
# The kmeans model looks at all the datapoints and randomly
# puts in the centroids on the graph
# It then reassigns the centroids to positions that are the average
# of the points
# closest to the centroids
# This process repeats until the centroids don't change their position very much
# I changed the amount of clusters mulitple times and ultimately chose to use 
# 2 clusters because it had the highest silhouette score
# the silhouette score is a number that ranges between -1 and 1, 
# it measures how good a kmeans clustering model is. 
# It's a measure of how seperated the clusters are and how similar the
# data points in each cluster are to each other
# A higher silohouette score is better


# kmeans = KMeans(n_clusters=3, random_state=11) 
# silhousette score = 0.4563365489027713

# kmeans = KMeans(n_clusters=4, random_state=11)
# silhousette score = 0.3671388738659935
 
# kmeans = KMeans(n_clusters=5, random_state=11) 
# silhousette score = 0.3753950985916534

# kmeans = KMeans(n_clusters=6, random_state=11) 
# silhousette score = 0.3620979792062964

# kmeans = KMeans(n_clusters=7, random_state=11)
# silhousette score = 0.3373364959897903

# kmeans = KMeans(n_clusters=10, random_state=11)
# silhousette score = 0.32807471339011796

kmeans = KMeans(n_clusters=2, random_state=11)
# silhousette score = 0.47183882768902063 

# kmeans = KMeans(n_clusters=2, random_state=40)
# silhousette score = 0.47176088219324963

# kmeans = KMeans(n_clusters=720, random_state=11)
# silhousette score = 0.2825110321447019

# This fits the kmeans model to the data
kmeans.fit(danger_data)

# labels = kmeans.fit_predict(danger_data)
# train_danger_df["clusters"] = labels
# print(train_danger_df)
# print(train_danger_df["clusters"].loc["0"])

# This gets the silhouette score
print(silhouette_score(danger_data, kmeans.fit_predict(danger_data)))

# This gets the centroids
centroids= kmeans.cluster_centers_
# Prepares the centroids to be plotted
centers = prepare_center(centroids, 3)

# Code lines 320-335 are from Scaler.com
# This sets up the figure
fig = plt.figure()
# This sets up the 3d graph
ax = fig.add_subplot(projection='3d')

# this assigns the data to their coressponding variables
post_x = train_danger_df["Horizontal_Distance_To_Fire_Points"]
post_y = train_danger_df["Horizontal_Distance_To_Hydrology"]
post_z = train_danger_df["Horizontal_Distance_To_Roadways"]

# This plots the datapoints
ax.scatter(post_x, post_y, post_z, c='r', marker='o', s=1)

# This labels the axes
ax.set_xlabel('Distance from Fire Points')
ax.set_ylabel('Distance From Water')
ax.set_zlabel('Distance From Roadways')

# This plots the centroids on the same graph as the datapoints
for i in range(len(centers)):
    ax.scatter(centers[i][0], centers[i][1], centers[i][2], s=100, c='k')
plt.show()

# Code lines 344-350 are from Scaler.com
# This sets up a new figure and 3d graph
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# This labels the axes
ax.set_xlabel('Distance from Fire Points')
ax.set_ylabel('Distance From Water')
ax.set_zlabel('Distance From Roadways')

# This plots the centoids on a graph without the other datapoints
for i in range(len(centers)):
    ax.scatter(centers[i][0], centers[i][1], centers[i][2], s=100, c='k')

plt.show()

# This gets the predictions for the testing data
# The model will predict how at risk a tree is based on how close it is to 
# water, fire points and roadways
# Loops through every test datapoint
for i in range(1161):
    points = []
    # Gets the x value of a datapoint
    x_1 = list(test_danger_df["Horizontal_Distance_To_Fire_Points"])[i]
    # Gets the y value of a datapoint
    y_1 = list(test_danger_df["Horizontal_Distance_To_Hydrology"])[i]
    # Gets the z value of a datapoint
    z_1 = list(test_danger_df["Horizontal_Distance_To_Roadways"])[i]

    # Appends the coordinates to a list
    points.append(x_1)
    points.append(y_1)
    points.append(z_1)

    # Finds the closest centroid to the points
    closest_centroid = get_closest_centroid(centers, points)
        
    # This finds out how at risk a tree is
    # If the point is closest to the first centroid in the list
    if closest_centroid == centers[0]:
        # then that test datapoint is at higher risk
        print("point" , x_1, ",", y_1, ",", z_1 ,"is higher risk" )
    # If the test data point is closest to the second centroid in the list
    elif closest_centroid == centers[1]:
        # then the test data point is at a lower risk
        print("point" , x_1, ",", y_1 , ",", z_1, "is lower risk")

# This code overall uses kmeans to train itself using distance from 
# fire points, water and roadways to make predtions on how at risk
# other trees are. 
