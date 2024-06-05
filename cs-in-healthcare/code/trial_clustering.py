# Arya Kuttiyan
# Computer Science in Healthcare
# May 8 2024
# The purpose of this program is to run kmeans clustering on clinical trial data

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

'''
The purpose of this function is to turns the coordinates of each centroid into
a 2d list. Ex: [[x_1, y_1], [x_2, y_2]

Parameters: A list of the coordinates of the centroids, it is in the 
this form: [[x_1 y_1], [x_2 y_2]

It also takes the dimensions of the graph. These centroids have x and y
coordinates, so I would input 2 dimensions.

Returns: A 2d list with sublists of the x and y coordinates of a centroid
'''
def prepare_center(centers, dimensions):
    # Initalize the list of centers
    center_list = []
    # Initalizes the sublist
    sublist = []
    i = 0
    # Looks at every centroid in the centroid list
    for center in centers:
        # Looks at every coordinate for the centroid (x, y)
        for point in center:
            # Appends the coordinate to a sublist
            sublist.append(point)
        # the sublist now has the x and y coordinate of the center
        # appends the sublist of these coordinates to a bigger list
        center_list.append(sublist[i:i + dimensions])
        # Increments i by the amount that the loop needs
        # to cycle through the rest of the centroids
        i += dimensions

    # returns the list of the centroids
    return center_list

# opens file of clinical data
patient_data = open("test_clinical_trial_data_2.csv")

# reads data
csv_reader = csv.reader(patient_data)

rows = []

# adds each row of the data to a list
for row in csv_reader:
    rows.append(row)

# samples data
sample_row = rows[1: 1461][0::10]
# Makes pandas dataframe
patient_data_frame = pd.DataFrame(sample_row, columns=rows[0])

# samples the data frame
sample_patient_data_frame = patient_data_frame.sample(frac=0.1, random_state=17)

print(sample_patient_data_frame)

# Initalizes list of the data
sampled = []
# Initalizes the sublists
sublist = []
j = 0
# This for loop prepares the training dataframe for kmeans
# It makes the data into a 2d list with each sublist representing each datapoint
# The sublists are in the form: [[x_1, y_1], [x_2, y_2, z_2], where x
# is the length of stay and y is the readdmision rate
# Looks at every data point
for i in range(len(list(sample_patient_data_frame["AGE"]))):
    # Appends the length of stay to a list
    sublist.append(list(sample_patient_data_frame["LOS"])[i])
    # Appends the redmission rate to a list
    sublist.append(list(sample_patient_data_frame["RAR"])[i])
    # adds the sublist a larger list
    sampled.append(sublist[j:j + 2])
    j += 2

print(sampled)

# Plots a scattor plot with the data frame
sns.set(font_scale=1.1)
sns.set_style('whitegrid')
grid = sns.scatterplot(x="LOS", y="RAR", hue="Assignment", data=sample_patient_data_frame)
#grid.set(x="Length_of_Stay", y_label="Rate_of_Readmission")
plt.show()

# runs KMeans on the data
kmeans = KMeans(n_clusters=3, random_state=11)
print(row[1 : 1461])
kmeans.fit(sampled)

# Gets the centroids
centroids= kmeans.cluster_centers_
print(centroids)
# Prepares the centroids to be plotted
centers = prepare_center(centroids, 2)

sns.scatterplot(x="LOS", y="RAR",  hue="Assignment", data=sample_patient_data_frame)

# Makes dataframe with the centroids
centers_data_frame = pd.DataFrame(data=centers,columns=["x", "y"] )

# Plots the centroids on the same graph as the data points
sns.scatterplot(x="x", y="y", data=centers_data_frame, s=100, c='k')
plt.show()

# Plots the centroids on a their own graph
sns.scatterplot(x="x", y="y", data=centers_data_frame, s=100, c='k')

plt.show()

patient_data.close()
