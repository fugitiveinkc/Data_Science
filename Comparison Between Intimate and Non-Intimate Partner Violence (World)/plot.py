'''

Title: Comparison Between Intimate and Non-Intimate Partner Violence (World)

Purpose: Using WHO data regarding sexual violence against women, this program will plot both intimate and non-intimate partner violence rates in the world to see how they compare.

Visual effect choice: Have two bars side by side for each age demographic

'''
#Step 0: Place libraries used here

import csv, re
from matplotlib import pyplot as plt

#Step 1: Import CSV files

intimate_file = open('Intimate.csv')
intimate_reader = csv.reader(intimate_file)
intimate_file = [row for row in intimate_reader]

non_intimate_file = open('Non-Intimate.csv')
non_intimate_reader = csv.reader(non_intimate_file)
non_intimate_file = [row for row in non_intimate_reader]


#Step 2: Extract needed data and labels

xlabels = [non_intimate_file[i][0] for i in range(4,12)]
x_test_labels = ['Africa', 'America', 'Eastern Mediterranean', 'Europe', 'South-East Asia', 'Western-Pacific', 'High-Income', 'World']
print xlabels
ylabel = "Sexual Violence Prevalence (%)"
non_intimate_values = [float(re.match('\d\d[.]\d|\d[.]\d|\d\d|\d', non_intimate_file[i][1]).group()) for i in range(4,12)]
intimate_values = [float(re.match('\d\d[.]\d|\d[.]\d|\d\d|\d', row[2]).group()) for row in intimate_file if re.search('15-69',row[1])]


#Step 3: Plot and format

xmarks_1 = [i + 0.1 for i, _ in enumerate(xlabels)]
plt.bar(xmarks_1, non_intimate_values, width=0.4, color='b')
xmarks_2 = [i + 0.5 for i, _ in enumerate(xlabels)]
plt.bar(xmarks_2, intimate_values, width=0.4, color='r')

plt.ylabel(ylabel)
plt.title("Non-Intimate vs. Intimate Partner Violence (Women, 2010)")
plt.xticks([i + 0.5 for i, _ in enumerate(xlabels)], x_test_labels) #problem here

plt.show()


#Step 4: Additional notes and improvements
#--Make a bit more readable
#--Put label for each color of bar
#--Figure out better xlabels
