# Arya Kuttiyan
# Computer Science in Healthcare
# June 4 2024
# The purpose of this code is to do data analysis on a dataset about dementia patients
# The questions I had were what is the connection between mental health and depression?
# What genetic factors are most impactful on dementia risk? What factors overall are most
# impactful on dementia risk?

# Reads in the file
import csv
# Data visualization
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Gets the standard deviation
import statistics

'''
This function looks at all the categories of a given feature and counts how
many people in each category have dementia.

Parameters: A integer that is the index of the feature in the top 
row of the data file.

Returns: A dictionary with the possible categories as keys
and the amount of people with dementia as the values.
'''
def find_num_dementia(index):

    # Initializes dictionary with the data
    data_dict = dict()
    all_possible_categories = []
    # Loops through every row exept the first row because that row has the titles
    for row in initial_rows[1:1001]:
        # It looks at part of the row that pertains to the feature we are looking at
        # If it finds a new category
        if row[index] not in all_possible_categories:
            # Adds the new category to the list of possible categories
            # This keeps track of all the categories in a feature
            # So that if there is ever a category that has no people with dementia
            # we can still keep track of that
            all_possible_categories.append(row[index])
        
        # If the person has dementia
        if row[21] == "1":
            # In the data dictionary add 1 to the amount of people of a certain category
            # This counts the amount of people in a certain category that has dementia
            try:
                data_dict[row[index]] += 1
            # If that category hasn't been initialized in the dictionary
            # Initalize the category
            except:
                data_dict[row[index]] = 1
    
    # Loop through all the possible categories
    for category in all_possible_categories:
        # If a category is not included in the dictionary
        # that means that the category has 0 people with dementia
        if category not in data_dict.keys():
            # Add that category to the dictionary and set the value to 0
            data_dict[category] = 0

    return data_dict

'''
The purpose of this function is to separate continuous data into ranges, 
so that the data become categorical. Then the function the amount of people
in each range that have dementia.

Parameters: An index that represents the index of the feature that we are looking
at on the first row of the data file. For example, the alcohol level is at index 1
on the first row of the data file, so if I wanted to split the alcohol levels 
into ranges I would input 1. Another parameter is a list of strings. Each string is 
the desired range. Another input is a 2 dimensional list. Eahc sublist represent the range as
well.

Returns: The function returns a dictionary where the keys are the ranges and 
the values are the number of people with dementia.

'''
def find_num_dementia_continuous(index, string_ranges, ints_ranges):

    num_dementia_dict = dict()

    # Loops through all the ranges in the string list
    for i in range(len(string_ranges)):
        # Initalizes each range as a key and the value set to 0
        num_dementia_dict[string_ranges[i]] = 0
    
    # Loops through each row in the data file except for the 1st row because 
    # the first row is the titles
    for row in initial_rows[1 : 1001]:
        # If the person has dementia
        if row[21] == "1":
            # Loops through all the possible ranges
            for i in range(len(ints_ranges) - 1):
                # Checks to see which range feature we are looking at fits into 
                if float(row[index]) >= float(ints_ranges[i][0]) and float(row[index]) < float(ints_ranges[i][1]):
                    # When the range the feature fits into is found
                    # 1 is added to the number of people in that range that have dementia
                    num_dementia_dict[string_ranges[i]] += 1
            # This is the final check
            # It needs to be out of the for loop because it needs a <= instead of a < for the second condition
            if float(row[index]) >= float(ints_ranges[i + 1][0]) and float(row[index]) <= float(ints_ranges[i + 1][1]):
                # When the range the feature fits into is found
                # 1 is added to the number of people in that range that have dementia
                num_dementia_dict[string_ranges[i + 1]] += 1
    
    return num_dementia_dict

# Opens data file
dementia_data_no_numbers = open("dementia_patients_health_data_not_numbered.csv")

# Reads the file into a csv reader
csv_reader = csv.reader(dementia_data_no_numbers)

# Loops through each row in the csv reader
initial_rows = []
for row in csv_reader:
    # appends each row into a list
    initial_rows.append(row)

####################### How is Mental Health Connected to Dementia? #################################

# Look at the the categoies of inactive, mildly active and moderatly active
# Sees how many people in each category have dementia
physical_activity_dict = find_num_dementia(14)

# Creates x values
activity = list(physical_activity_dict.keys())

# creates y values
dementia = list(physical_activity_dict.values())

# Creates bar chart of data
fig = plt.figure(figsize=(10,10))
plt.bar(activity, dementia, color="blue", width=0.4)
plt.xlabel("Physical Activity")
plt.ylabel("Number of People with Dementia")
plt.title("Physical Activity vs. Dementia")
plt.show()
# The data doesn't show much of a connection between physical activity and dementia
# Studies show however that physical activity can reduce the risk of dementia
# https://www.health.harvard.edu/mind-and-mood/even-light-physical-activity-may-help-prevent-dementia

# Looks at how many people that get poor sleep have dementia and how many people that
# have good sleep have dementia
sleep_dict = find_num_dementia(19)

# Makes x values
sleep_activity = list(sleep_dict.keys())

# Makes y values
dementia = list(sleep_dict.values())

# Plots bar chart
fig = plt.figure(figsize=(10,10))
plt.bar(sleep_activity, dementia, color="blue", width=0.4)
plt.xlabel("Sleep Activity")
plt.ylabel("Number of People with Dementia")
plt.title("Sleep Activity vs. Dementia")
plt.show()
# The data shows that those with poor sleep have more dementia
# However both the poor and good sleep both show pretty similar numbers for people with dementia
# Studies suggest that not enough sleep or too much sleep can increase the risk of dementia
# These studies don't show if this is a cause of dementia or a symptom of dementia
# Later studies suggest that lack of sleep can cause dementia
# https://www.nih.gov/news-events/nih-research-matters/lack-sleep-middle-age-may-increase-dementia-risk

#print(find_num_dementia(7))
# Find how many people of different blood alcohol levels have dementia
alcohol_dementia_dictionary = find_num_dementia_continuous(1, ["0 - 0.05", "0.05 - 0.1", "0.1 - 0.15", "0.15 - 0.2"], [[0, 0.05], [0.05, 0.1], [0.1, 0.15], [0.15, 0.2]])

# Makes x values
levels = list(alcohol_dementia_dictionary.keys())
# Makes y values
dementia = list(alcohol_dementia_dictionary.values())

# Makes a bar graph
fig = plt.figure(figsize=(10,10))
plt.bar(levels, dementia, color="blue", width=0.4)
plt.xlabel("Alcohol Blood Level")
plt.ylabel("Number of People with Dementia")
plt.title("Alcohol Level vs. Dementia")
plt.show()
# Data shows that people between the 0 - 0.05 alcohol blood level range has the most dementia
# compared to the other ranges
# There doesn't seem to be that much of a connection between alcohol and Dementia seen in this dataset
# Studies show that people who increase the amount of alcohol they drink and people that quit alcohol
# have higher risk for dementia
# This is not certain because someone may quit drinking because their health has worsened
# So the connection of worsened health may not be caused by quitting drinking
# Quitting drinking might be caused by worsening health
# https://www.npr.org/2023/02/18/1157797844/alcohol-drinking-dementia-risk-south-korea-study

# Finds the number of people that are former smokers, never smoked or current smokers
# and how many of those people have dementia
smoking_dict = find_num_dementia(12)

# Makes x values
smoking = list(smoking_dict.keys())

# Makes y values
dementia = list(smoking_dict.values())

# Plots bar chart
fig = plt.figure(figsize=(10,10))
plt.bar(smoking, dementia, color="blue", width=0.4)
plt.xlabel("Smoking Habits")
plt.ylabel("Number of People with Dementia")
plt.title("Smoking Habits vs. Dementia")
plt.show()
# Current smokers never had dementia in this dataset
# People that never smoked however had less dementia than people that were former smokers
# However the number of people with dementia for the former smokers and peopel that
# had never smoked was almost equal
# Studies show that smoking increases risk of dementia
# but nicotine helps with reaction time, learning and memory
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2642819/

# Finds how many people have depression and how many people don't
# and how many of these people have dementia
depression_dict = find_num_dementia(15)

# Makes x values
depression = list(depression_dict.keys())
# Makes y values
dementia = list(depression_dict.values())

# Creates bar chart
fig = plt.figure(figsize=(10,10))
plt.bar(depression, dementia, color="blue", width=0.4)
plt.xlabel("Depression Status")
plt.ylabel("Number of People with Dementia")
plt.title("Depression Status vs. Dementia")
plt.show()
# The data doesn't show a connection between depression and dementia
# Studies show that dementia increases risk and is also an early symptome that
# indicates the onset of dementia
# The studies aren't conclusive
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3039168/#:~:text=Approximately%2C%20half%20of%20the%20patients,as%20a%20prodrome%20of%20dementia.

########################### What genetic factors are the most impactful for dementia? #############################

# Finds how many male people have dementia and how many female people have dementia
sex_dict = find_num_dementia(10)

# Makes x values
sex = list(sex_dict.keys())

# Makes y values
dementia = list(sex_dict.values())

# Makes bar chart
fig = plt.figure(figsize=(10,10))
plt.bar(sex, dementia, color="green", width=0.4)
plt.xlabel("Sex")
plt.ylabel("Number of People with Dementia")
plt.title("Sex vs. Dementia")
plt.show()
# Data doesn't show connection between the gender and dementia
# Studies show that women are more likely to get dementia
# Women live longer, autoimmune diseases are more common in women + more reasons
# https://www.health.harvard.edu/blog/why-are-women-more-likely-to-develop-alzheimers-disease-202201202672

# Finds how many people have dementia that have a family history of dementia 
# and don't have a family history of dementia
family_history_dict = find_num_dementia(11)

# Makes x values
family_history = list(family_history_dict.keys())

# Makes y values
dementia = list(family_history_dict.values())

# Creates bar graph
fig = plt.figure(figsize=(10,10))
plt.bar(family_history, dementia, color="green", width=0.4)
plt.xlabel("Family History")
plt.ylabel("Number of People with Dementia")
plt.title("Family History vs. Dementia")
plt.show()
# There doesn't seem to be much of a connection because both categories
# have around the same amount of people with dementia
# Slightly more people without family history have dementia
# Studies show that family history increases the risk of dementia
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8689157/#:~:text=The%20average%20lifetime%20risk%20of,a%20family%20history%20of%20dementia.&text=This%20increased%20risk%20can%20be,on%20from%20parents%20to%20offspring.

# Check how many people have dementia with negative or positive apoe4 gene 
apoe_E4_dict = find_num_dementia(13)

# Makes x values
gene = list(apoe_E4_dict.keys())

# Makes y values
dementia = list(apoe_E4_dict.values())

# Makes bar chart
fig = plt.figure(figsize=(10,10))
plt.bar(gene, dementia, color="green", width=0.4)
plt.xlabel("Presence of APOE_ε4")
plt.ylabel("Number of People with Dementia")
plt.title("Presence of APOE_ε4 vs. Dementia")
plt.show()
# Most people with the gene have dementia
# Studies show that this gene increases risk of dementia
# https://www.nia.nih.gov/news/study-reveals-how-apoe4-gene-may-increase-risk-dementia.

############################ What factors are most impactful in dementia? #################################33
# Finds the number of people that have dementia in ranges for all the continuous features
alcohol_dict = find_num_dementia_continuous(1, ["0 - 0.05", "0.05 - 0.1", "0.1 - 0.15", "0.15 - 0.2"], [[0, 0.05], [0.05, 0.1], [0.1, 0.15], [0.15, 0.2]])
heart_beat_dict = find_num_dementia_continuous(2, ["60 - 70", "70 - 80", "80 - 90", "90 - 100"], [[60, 70], [70, 80], [80, 90], [90, 100]])
blood_oxygen_dict = find_num_dementia_continuous(3, ["90 - 95", "95 - 100"], [[90, 95], [95, 100]])
body_temperature_dict = find_num_dementia_continuous(4, ["36 - 36.75", "36.75 - 37.5"], [[36, 36.75], [36.75, 37.5]])
weight_dict = find_num_dementia_continuous(5, ["50 - 60", "60 - 70", "70 - 80", "80 - 90", "90 - 100"], [[50, 60], [60, 70], [70, 80], [80, 90], [90, 100]])
mri_delay_dict = find_num_dementia_continuous(6, ["0.09 - 15", "15 - 30", "30 - 45", "45 - 60"], [[0.09, 15], [15, 30], [30, 45], [45, 60]])
age_dict = find_num_dementia_continuous(7, ["60 - 70", "70 - 80", "80 - 90"], [[60, 70], [70, 80], [80, 90]])
cognitive_test_scores_dict = find_num_dementia_continuous(16, ["0 - 3", "3 - 6", "6 - 10"], [[0, 3], [3, 6], [6, 10]])


std_dict = dict()
# Loops through all the categorical features
for i in [0, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20]:
    # Finds the number of people that have dementia in each category
    dictionary = find_num_dementia(i)
    #print(dictionary.values())
    # Finds the standard deviation of the
    # people that have dementia in each category
    std = statistics.stdev(list(dictionary.values()))
    # Adds the standard deviation to a dictionary
    std_dict[initial_rows[0][i]] = std

# Finds the standard deviation of the number of people with dementia
# for all the continuous data dictionaries
# Adds the standard deviations to the standard deviation dictionary
std = statistics.stdev(list(alcohol_dict.values()))
std_dict[initial_rows[0][1]] = std

std = statistics.stdev(list(heart_beat_dict.values()))
std_dict[initial_rows[0][2]] = std

std = statistics.stdev(list(blood_oxygen_dict.values()))
std_dict[initial_rows[0][3]] = std

std = statistics.stdev(list(body_temperature_dict.values()))
std_dict[initial_rows[0][4]] = std

std = statistics.stdev(list(weight_dict.values()))
std_dict[initial_rows[0][5]] = std

std = statistics.stdev(list(mri_delay_dict.values()))
std_dict[initial_rows[0][6]] = std

std = statistics.stdev(list(age_dict.values()))
std_dict[initial_rows[0][7]] = std

std = statistics.stdev(list(cognitive_test_scores_dict.values()))
std_dict[initial_rows[0][16]] = std

# Sorts the standard deviations in decending order
sorted_std_dict = sorted(std_dict.values(), reverse=True)

sorted_keys = []
used_keys = []
# Loops through every number in the sorted list
for num in sorted_std_dict:
    # Finds which key corresponds to the standard deviation
    for key in std_dict.keys():
        if std_dict[key] == num:
            # This is for when multiple keys have the same standard deviation
            # If we haven't seen the key before
            if key not in used_keys:
                # Add the key to the seen keys list
                used_keys.append(key)
                # Add the key to the sorted keys list
                sorted_keys.append(key)

# Top 5: APOE_4, Smoking Status, Chronic Health Conditions, Education Level, Cognitive Test Scores

# Makes bar chart of apoe4 gene
fig = plt.figure(figsize=(10,10))
plt.bar(gene, dementia, color="purple", width=0.4)
plt.xlabel("Presence of APOE_ε4")
plt.ylabel("Number of People with Dementia")
plt.title("Presence of APOE_ε4 vs. Dementia")
plt.show()
# Most people with the gene have dementia
# Studies show that this gene increases risk of dementia
# https://www.nia.nih.gov/news/study-reveals-how-apoe4-gene-may-increase-risk-dementia

# Makes bar chart of smoking status
smoking = list(smoking_dict.keys())
dementia = list(smoking_dict.values())

fig = plt.figure(figsize=(10,10))
plt.bar(smoking, dementia, color="purple", width=0.4)
plt.xlabel("Smoking Habits")
plt.ylabel("Number of People without Dementia")
plt.title("Smoking Habits vs. Dementia")
plt.show()
# Current smokers never had dementia in this dataset
# People that never smoked however had less dementia than people that were former smokers
# However the number of people with dementia for the former smokers and peopel that
# had never smoked was almost equal
# Studies show that smoking increases risk of dementia
# but nicotine helps with reaction time, learning and memory
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2642819/

# Makes bar chart for chronic health conditions
chronic_health_conditions_dict = find_num_dementia(20)
chronic_health_conditions = list(chronic_health_conditions_dict.keys())
dementia = list(chronic_health_conditions_dict.values())

fig = plt.figure(figsize=(10,10))
plt.bar(chronic_health_conditions, dementia, color="purple", width=0.4)
plt.xlabel("Chronic Health Conditions")
plt.ylabel("Number of People with Dementia")
plt.title("Chronic Health Conditions vs. Dementia")
plt.show()
# People with diabetes have more dementia
# That might just be because a lot of people in this dataset had dementia
# Studies show that diabetes increases risk of dementia
# Studies also show that heart disease causes dementia
# Studies also show that hypertension causes dementia
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3641811/#:~:text=Coronary%20artery%20disease%20may%20lead,with%20brain%20small%20vessel%20disease.&text=Small%20vessel%20disease%20in%20turn,increased%20susceptibility%20to%20neurological%20insults.
# https://www.health.harvard.edu/blog/whats-the-relationship-between-diabetes-and-dementia-202107122546
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3181842/

# Makes bar chart for education level
education_level_dict = find_num_dementia(8)
education_level = list(education_level_dict.keys())
dementia = list(education_level_dict.values())

fig = plt.figure(figsize=(10,10))
plt.bar(education_level, dementia, color="purple", width=0.4)
plt.xlabel("Education Level")
plt.ylabel("Number of People with Dementia")
plt.title("Education Level vs. Dementia")
plt.show()
# People with a diploma and higher degree have less dementia according to the data
# There's also less people with a diploma and higher education in the dataset
# So that might have skewed the results
# Studies show that higher education may lower the risk of dementia
# It is suggested that education helps develope more synapses
# People that are more educated could be more aware about practices that are bad for health
# https://www.hopkinsmedicine.org/health/wellness-and-prevention/does-higher-learning-combat-dementia

# Makes bar chart cognitive test scores
cognitive_test_scores_dict = find_num_dementia_continuous(16, ["0 - 3", "3 - 6", "6 - 10"], [[0, 3], [3, 6], [6, 10]])
cognitive_test_scores = list(cognitive_test_scores_dict.keys())
dementia = list(cognitive_test_scores_dict.values())

fig = plt.figure(figsize=(10,10))
plt.bar(cognitive_test_scores, dementia, color="purple", width=0.4)
plt.xlabel("Cognitive Test Scores")
plt.ylabel("Number of People with Dementia")
plt.title("Cognitive Test Scores vs. Dementia")
plt.show()
# People with higher test scores have less dementia
# Cognitive tests are used to help diagnose dementia
# Studies show that low cognitive test scores increase the risk of dementia
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8203214/
