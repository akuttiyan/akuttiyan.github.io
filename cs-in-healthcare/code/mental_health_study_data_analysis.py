# Arya Kuttiyan
# Computer Science In Healthcare
# 4/16/2024
# This program looks at the mental health of medical school students and 
# visualizes and explores the data to try and find a connection 
# between the language spoken and mental health

import csv 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statistics

# Dataset from https://zenodo.org/records/5702895#.Y8OraNJBwUE
# opens file with data
mental_health_study_data = open('Data Carrard et al. 2022 MedTeach.csv')

# reads in the data in the file
csv_reader = csv.reader(mental_health_study_data)

initial_rows = []
# Puts all the rows in a file in a list
for row in csv_reader:
    initial_rows.append(row)

sub_row = []
data_dict = {}
j = 0

for i in range(7):
    # Loops through every row exept the first row because that row has the titles
    for row in initial_rows[1:887]:
        # appends the value in a row from a certain column to a list
        sub_row.append(int(row[i]))

    # Adds all the values in the column to a dictionary
    data_dict[initial_rows[0][i]] = sub_row[j : j + 886]
    j += 886

    # prints the average, median, mode and standard deviation for each column
    print()
    print("average", initial_rows[0][i], statistics.mean(data_dict[initial_rows[0][i]]))
    print("median", initial_rows[0][i], statistics.median(data_dict[initial_rows[0][i]]))
    print("mode", initial_rows[0][i], statistics.mode(data_dict[initial_rows[0][i]]))
    print("standard deviation", initial_rows[0][i], statistics.stdev(data_dict[initial_rows[0][i]]))
    print()

averaged_psyt_dict = dict()

sum_list = []

for i in [1, 15, 20, 37, 54, 60, 63, 90, 92, 95, 98, 102, 104, 106, 108, 114, 118, 120, 121]:
    for row in initial_rows[1 : 887]:
        if int(row[0]) == i:
                sum_list.append(int(row[1]))
    print(sum_list)
    if sum_list != []:
        average = statistics.mean(sum_list)
    sum_list = []
    

    if i == 1:
        averaged_psyt_dict["French"] = average
    elif i == 15:
        averaged_psyt_dict["German"] = average
    elif i == 20:
        averaged_psyt_dict["English"] = average
    elif i == 37:
        averaged_psyt_dict["Arab"] = average
    elif i == 54:
        averaged_psyt_dict["Chinese"] = average
    elif i == 60:
        averaged_psyt_dict["Croation"] = average
    elif i == 63:
        averaged_psyt_dict["Spanish"] = average
    elif i == 90:
        averaged_psyt_dict["Italian"] = average
    elif i == 92:
        averaged_psyt_dict["Japanese"] = average
    elif i == 95:
        averaged_psyt_dict["Lithuanian"] = average
    elif i == 98:
        averaged_psyt_dict["Dutch"] = average
    elif i == 102:
        averaged_psyt_dict["Portuguese"] = average
    elif i == 104:
        averaged_psyt_dict["Romanian"] = average
    elif i == 106:
        averaged_psyt_dict["Russian"] = average
    elif i == 108:
        averaged_psyt_dict["Serbian"] = average
    elif i == 114:
        averaged_psyt_dict["Swedish"] = average
    elif i == 118:
        averaged_psyt_dict["Turkish"] = average
    elif i == 120:
        averaged_psyt_dict["Vietnamese"] = average
    elif i == 121:
        averaged_psyt_dict["Other"] = average


languages = list(averaged_psyt_dict.keys())

psyt = list(averaged_psyt_dict.values())

fig = plt.figure(figsize=(20,10))
plt.bar(languages, psyt, color="maroon", width=0.4)
plt.xlabel("Languages")
plt.ylabel("Average for Who Saw a Therapist in the last six months (0 = no, 1 = yes)")
plt.title("Language vs. Average Therapy Visits")
plt.show()

sum_list = []
averaged_cesd_dict = dict()
for i in [1, 15, 20, 37, 54, 60, 63, 90, 92, 95, 98, 102, 104, 106, 108, 114, 118, 120, 121]:
    for row in initial_rows[1 : 887]:
        if int(row[0]) == i:
                print("yes")
                
                sum_list.append(int(row[2]))
    #print(sum_list)
    if sum_list != []:
        average = statistics.mean(sum_list)
    sum_list = []

    if i == 1:
        averaged_cesd_dict["French"] = average
    elif i == 15:
        averaged_cesd_dict["German"] = average
    elif i == 20:
        averaged_cesd_dict["English"] = average
    elif i == 37:
        averaged_cesd_dict["Arab"] = average
    elif i == 54:
        averaged_cesd_dict["Chinese"] = average
    elif i == 60:
        averaged_cesd_dict["Croation"] = average
    elif i == 63:
        averaged_cesd_dict["Spanish"] = average
    elif i == 90:
        averaged_cesd_dict["Italian"] = average
    elif i == 92:
        averaged_cesd_dict["Japanese"] = average
    elif i == 95:
        averaged_cesd_dict["Lithuanian"] = average
    elif i == 98:
        averaged_cesd_dict["Dutch"] = average
    elif i == 102:
        averaged_cesd_dict["Portuguese"] = average
    elif i == 104:
        averaged_cesd_dict["Romanian"] = average
    elif i == 106:
        averaged_cesd_dict["Russian"] = average
    elif i == 108:
        averaged_cesd_dict["Serbian"] = average
    elif i == 114:
        averaged_cesd_dict["Swedish"] = average
    elif i == 118:
        averaged_cesd_dict["Turkish"] = average
    elif i == 120:
        averaged_cesd_dict["Vietnamese"] = average
    elif i == 121:
        averaged_cesd_dict["Other"] = average

languages = list(averaged_cesd_dict.keys())

cesd = list(averaged_cesd_dict.values())
print(cesd)

fig = plt.figure(figsize=(20,10))
plt.bar(languages, cesd, color="maroon", width=0.4)
plt.xlabel("Languages")
plt.ylabel("Average of CESD scale, values range from 0 to 60, the higher the more depressed someone is")
plt.title("Language vs. CESD Scale")
plt.show()

sum_list = []
averaged_stai_t_dict = dict()
for i in [1, 15, 20, 37, 54, 60, 63, 90, 92, 95, 98, 102, 104, 106, 108, 114, 118, 120, 121]:
    for row in initial_rows[1 : 887]:
        if int(row[0]) == i:
                print("yes")
                sum_list.append(int(row[3]))
    #print(sum_list)
    if sum_list != []:   
        average = statistics.mean(sum_list)
    sum_list = []
    if i == 1:
        averaged_stai_t_dict["French"] = average
    elif i == 15:
        averaged_stai_t_dict["German"] = average
    elif i == 20:
        averaged_stai_t_dict["English"] = average
    elif i == 37:
        averaged_stai_t_dict["Arab"] = average
    elif i == 54:
        averaged_stai_t_dict["Chinese"] = average
    elif i == 60:
        averaged_stai_t_dict["Croation"] = average
    elif i == 63:
        averaged_stai_t_dict["Spanish"] = average
    elif i == 90:
        averaged_stai_t_dict["Italian"] = average
    elif i == 92:
        averaged_stai_t_dict["Japanese"] = average
    elif i == 95:
        averaged_stai_t_dict["Lithuanian"] = average
    elif i == 98:
        averaged_stai_t_dict["Dutch"] = average
    elif i == 102:
        averaged_stai_t_dict["Portuguese"] = average
    elif i == 104:
        averaged_stai_t_dict["Romanian"] = average
    elif i == 106:
        averaged_stai_t_dict["Russian"] = average
    elif i == 108:
        averaged_stai_t_dict["Serbian"] = average
    elif i == 114:
        averaged_stai_t_dict["Swedish"] = average
    elif i == 118:
        averaged_stai_t_dict["Turkish"] = average
    elif i == 120:
        averaged_stai_t_dict["Vietnamese"] = average
    elif i == 121:
        averaged_stai_t_dict["Other"] = average

languages = list(averaged_stai_t_dict.keys())

stai_t = list(averaged_stai_t_dict.values())
print(stai_t)

fig = plt.figure(figsize=(20,10))
plt.bar(languages, stai_t, color="maroon", width=0.4)
plt.xlabel("Languages")
plt.ylabel("State Trait Anxiety Inventory. Ranges from 20-80. Higher score mean higher anxiety.")
plt.title("Language vs. State Trait Anxiety Inventory Scale")
plt.show()

sum_list = []
averaged_mbi_ex_dict = dict()
for i in [1, 15, 20, 37, 54, 60, 63, 90, 92, 95, 98, 102, 104, 106, 108, 114, 118, 120, 121]:
    for row in initial_rows[1 : 887]:
        if int(row[0]) == i:
                print("yes")
                sum_list.append(int(row[4]))
    #print(sum_list)
    if sum_list != []:   
        average = statistics.mean(sum_list)
    sum_list = []
    if i == 1:
        averaged_mbi_ex_dict["French"] = average
    elif i == 15:
        averaged_mbi_ex_dict["German"] = average
    elif i == 20:
        averaged_mbi_ex_dict["English"] = average
    elif i == 37:
        averaged_mbi_ex_dict["Arab"] = average
    elif i == 54:
        averaged_mbi_ex_dict["Chinese"] = average
    elif i == 60:
        averaged_mbi_ex_dict["Croation"] = average
    elif i == 63:
        averaged_mbi_ex_dict["Spanish"] = average
    elif i == 90:
        averaged_mbi_ex_dict["Italian"] = average
    elif i == 92:
        averaged_mbi_ex_dict["Japanese"] = average
    elif i == 95:
        averaged_mbi_ex_dict["Lithuanian"] = average
    elif i == 98:
        averaged_mbi_ex_dict["Dutch"] = average
    elif i == 102:
        averaged_mbi_ex_dict["Portuguese"] = average
    elif i == 104:
        averaged_mbi_ex_dict["Romanian"] = average
    elif i == 106:
        averaged_mbi_ex_dict["Russian"] = average
    elif i == 108:
        averaged_mbi_ex_dict["Serbian"] = average
    elif i == 114:
        averaged_mbi_ex_dict["Swedish"] = average
    elif i == 118:
        averaged_mbi_ex_dict["Turkish"] = average
    elif i == 120:
        averaged_mbi_ex_dict["Vietnamese"] = average
    elif i == 121:
        averaged_mbi_ex_dict["Other"] = average

languages = list(averaged_mbi_ex_dict.keys())

mbi_ex = list(averaged_mbi_ex_dict.values())
print(mbi_ex)

fig = plt.figure(figsize=(20,10))
plt.bar(languages, mbi_ex, color="maroon", width=0.4)
plt.xlabel("Languages")
plt.ylabel("MBI Exhaustion Scale. Ranges from 0 to 54")
plt.title("Language vs. MBI Exhaustion Scale")
plt.show()

sum_list = []
averaged_mbi_cy_dict = dict()
for i in [1, 15, 20, 37, 54, 60, 63, 90, 92, 95, 98, 102, 104, 106, 108, 114, 118, 120, 121]:
    for row in initial_rows[1 : 887]:
        if int(row[0]) == i:
                print("yes")
                sum_list.append(int(row[5]))
    #print(sum_list)
    if sum_list != []:   
        average = statistics.mean(sum_list)
    sum_list = []
    if i == 1:
        averaged_mbi_cy_dict["French"] = average
    elif i == 15:
        averaged_mbi_cy_dict["German"] = average
    elif i == 20:
        averaged_mbi_cy_dict["English"] = average
    elif i == 37:
        averaged_mbi_cy_dict["Arab"] = average
    elif i == 54:
        averaged_mbi_cy_dict["Chinese"] = average
    elif i == 60:
        averaged_mbi_cy_dict["Croation"] = average
    elif i == 63:
        averaged_mbi_cy_dict["Spanish"] = average
    elif i == 90:
        averaged_mbi_cy_dict["Italian"] = average
    elif i == 92:
        averaged_mbi_cy_dict["Japanese"] = average
    elif i == 95:
        averaged_mbi_cy_dict["Lithuanian"] = average
    elif i == 98:
        averaged_mbi_cy_dict["Dutch"] = average
    elif i == 102:
        averaged_mbi_cy_dict["Portuguese"] = average
    elif i == 104:
        averaged_mbi_cy_dict["Romanian"] = average
    elif i == 106:
        averaged_mbi_cy_dict["Russian"] = average
    elif i == 108:
        averaged_mbi_cy_dict["Serbian"] = average
    elif i == 114:
        averaged_mbi_cy_dict["Swedish"] = average
    elif i == 118:
        averaged_mbi_cy_dict["Turkish"] = average
    elif i == 120:
        averaged_mbi_cy_dict["Vietnamese"] = average
    elif i == 121:
        averaged_mbi_cy_dict["Other"] = average

languages = list(averaged_mbi_cy_dict.keys())

mbi_cy = list(averaged_mbi_cy_dict.values())
print(mbi_cy)

fig = plt.figure(figsize=(20,10))
plt.bar(languages, mbi_cy, color="maroon", width=0.4)
plt.xlabel("Languages")
plt.ylabel("MBI Cynicism Scale. Ranges from 0 to 54")
plt.title("Language vs. MBI Cynicism")
plt.show()

sum_list = []
averaged_mbi_ea_dict = dict()
for i in [1, 15, 20, 37, 54, 60, 63, 90, 92, 95, 98, 102, 104, 106, 108, 114, 118, 120, 121]:
    for row in initial_rows[1 : 887]:
        if int(row[0]) == i:
                print("yes")
                sum_list.append(int(row[6]))
    #print(sum_list)
    if sum_list != []:   
        average = statistics.mean(sum_list)
    sum_list = []
    if i == 1:
        averaged_mbi_ea_dict["French"] = average
    elif i == 15:
        averaged_mbi_ea_dict["German"] = average
    elif i == 20:
        averaged_mbi_ea_dict["English"] = average
    elif i == 37:
        averaged_mbi_ea_dict["Arab"] = average
    elif i == 54:
        averaged_mbi_ea_dict["Chinese"] = average
    elif i == 60:
        averaged_mbi_ea_dict["Croation"] = average
    elif i == 63:
        averaged_mbi_ea_dict["Spanish"] = average
    elif i == 90:
        averaged_mbi_ea_dict["Italian"] = average
    elif i == 92:
        averaged_mbi_ea_dict["Japanese"] = average
    elif i == 95:
        averaged_mbi_ea_dict["Lithuanian"] = average
    elif i == 98:
        averaged_mbi_ea_dict["Dutch"] = average
    elif i == 102:
        averaged_mbi_ea_dict["Portuguese"] = average
    elif i == 104:
        averaged_mbi_ea_dict["Romanian"] = average
    elif i == 106:
        averaged_mbi_ea_dict["Russian"] = average
    elif i == 108:
        averaged_mbi_ea_dict["Serbian"] = average
    elif i == 114:
        averaged_mbi_ea_dict["Swedish"] = average
    elif i == 118:
        averaged_mbi_ea_dict["Turkish"] = average
    elif i == 120:
        averaged_mbi_ea_dict["Vietnamese"] = average
    elif i == 121:
        averaged_mbi_ea_dict["Other"] = average

languages = list(averaged_mbi_ea_dict.keys())

mbi_ea = list(averaged_mbi_ea_dict.values())
print(mbi_ea)

fig = plt.figure(figsize=(20,10))
plt.bar(languages, mbi_ea, color="maroon", width=0.4)
plt.xlabel("Languages")
plt.ylabel("MBI Professional Efficacy Scale. Ranges from 0 to 54")
plt.title("Language vs. MBI Professional Efficacy Scale")
plt.show()
