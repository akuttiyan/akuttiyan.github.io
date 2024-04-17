# Arya Kuttiyan
# Computer Science In Healthcare
# 4/16/2024
# This program looks at patient data about patients in a lung cancer study and 
# visualizes and explores the data to try and find patterns and trends

import csv # From Analytics Vidhya
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statistics

# opens file with data
patient_data = open('cs-in-healthcare\code\cancer_patient_data.csv') # From Analytics Vidhya

# reads in the data in the file
csv_reader = csv.reader(patient_data) # From Analytics Vidhya

initial_rows = []
# Puts all the rows in a file in a list
for row in csv_reader:
    initial_rows.append(row)


sub_row = []
data_dict = {}
j = 0

# Loops through every row in the list and places the data into a 
# dictionary where the keys are the column titles that map to the values in the column
for i in range(1, 24):
    # Loops through every row exept the first row because that row has the titles
    for row in initial_rows[1:1001]:
        # appends the value in a row from a certain column to a list
        sub_row.append(int(row[i]))

    # Adds all the values in the column to a dictionary
    data_dict[initial_rows[0][i]] = sub_row[j : j + 1000]
    j += 1000

    # prints the average, median, mode and standard deviation for each column
    print()
    print("average", initial_rows[0][i], statistics.mean(data_dict[initial_rows[0][i]]))
    print("median", initial_rows[0][i], statistics.median(data_dict[initial_rows[0][i]]))
    print("mode", initial_rows[0][i], statistics.mode(data_dict[initial_rows[0][i]]))
    print("standard deviation", initial_rows[0][i], statistics.stdev(data_dict[initial_rows[0][i]]))
    print()

# sets a up a data frame of all the patient data
patient_data_frame = pd.DataFrame(data_dict)

print(patient_data_frame)

# sets up the font and style of a graph
sns.set (font_scale=1.1)
sns.set_style('whitegrid')

# plots a genetic risk vs. chronic lung disease graph
graph = sns.scatterplot(data=patient_data_frame, x=patient_data_frame["Genetic Risk"], y=patient_data_frame["chronic Lung Disease"])
plt.show()
# With higher genetic risk more people have chronic lung disease, and with lower genetic risk less people have chronic lung disease

# plots an Age vs. Swallowing Difficulty Graph
graph = sns.scatterplot(data=patient_data_frame, x=patient_data_frame["Age"], y=patient_data_frame["Swallowing Difficulty"]) 
plt.show()
# More people in between their 30s and 50s had swallowing difficulty , while the amount of swalowing difficulty decreased towards age 70
# Altough there might just be less data on older patients, making it look like there are fewer older patients that experience swallowing difficulty

# plots an Air Pollution vs. Chronic Lung Disease graph
graph = sns.scatterplot(data=patient_data_frame, x=patient_data_frame["Air Pollution"], y=patient_data_frame["chronic Lung Disease"]) 
plt.show()
# Even people with air pollution levels of 1, experienced chronic lung disease levels up to 6.
# Air pollution also has the 2nd highest standard deviation so the data is very spread out across the graph

graph = sns.scatterplot(data=patient_data_frame, x=patient_data_frame["Age"], y=patient_data_frame["Fatigue"]) 
plt.show()
# There doesn't seem to be much of a correlation between Age and Fatigue

graph = sns.scatterplot(data=patient_data_frame, x=patient_data_frame["Smoking"], y=patient_data_frame["Snoring"]) 
plt.show()
# There doesn't seem to be much of a correlation between smoking and snoring

graph = sns.scatterplot(data=patient_data_frame, x=patient_data_frame["Smoking"], y=patient_data_frame["Wheezing"]) 
plt.show()
# Even people that smoke less have higher wheezing levels

graph = sns.scatterplot(data=patient_data_frame, x=patient_data_frame["Smoking"], y=patient_data_frame["Shortness of Breath"]) 
plt.show()
# Even people who smoke less have higher levels of shortness of breath too