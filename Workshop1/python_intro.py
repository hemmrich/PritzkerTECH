#First, we import a module (called "pandas") that will help us read our downloaded CSV (comma separated values) file.
#By importing it as "pd," we can now refer back to it as "pd" instead of typing out "pandas" every time. 

import pandas as pd

#Now we will use pd's function "read_csv" to create a data table that we can manipulate.
#We assign a name to the table (health_data) using "=".
#Within the parentheses, we type the file name exactly as it appears in our working directory (desktop). 

health_data = pd.read_csv("Public_Health_Statistics-_Selected_public_health_indicators_by_Chicago_community_area.csv")
print health_data.head()

#This will give you the first five rows of data to preview how it looks.
#Notice that the columns are named at the top. Let's isolate a specific column by using brackets and parentheses.

birth_rate = health_data["Birth Rate"]
print birth_rate.head()

#This gives you the first 5 values of the birth rate column. Notice that rows are indexed starting at 0.
#Try on your own to isolate the "General Fertility Rate" column and print out the first five values of the column.

#Let's isolate just the first row of the birth rate column.

birth_rate_first_row = health_data["Birth Rate"][0]
print birth_rate_first_row

#Now try this. You should get the same value. Do you understand why?

print birth_rate[0]

#Try on your own to print the 7th value of the "General Fertility Rate" column.

#Now let's do some math. Take the average and standard deviation of the birth_rate column.

print birth_rate.mean()
print birth_rate.std()

#On your own, do the same for the General Fertility Rate column.

#I wonder if the mean and standard deviation are the correct measures of center and spread.
#Let's make a histogram to find out!
#Here we'll use a module called matplotlib.

import matplotlib.pyplot as plt

plt.hist(birth_rate, edgecolor = "black")
plt.title("Distribution of Birth Rates")
plt.ylabel("Frequency")
plt.xlabel("Birth Rates")
plt.show()

#Yikes. Doesn't look like a normal distribution. Does the General Fertility Rate column show a normal distribution?
#Let's check out the median and IQR.
#We'll have to calculate the IQR by importing a module called numpy and using its percentile function.
#Notice that the percentile function accepts certain values within the parentheses, separated by commas.
#We call these values "arguments." Different functions accept different kinds of arguments.
#For this particular function (percentile), the first argument is our data (birth rate column).
#The second argument is the percentile we are looking for (25, 50, etc.)

import numpy as np

first_quartile = np.percentile(birth_rate, 25)
third_quartile = np.percentile(birth_rate, 75)
iqr = third_quartile - first_quartile
print iqr

#What is the IQR of the General Fertility Rate column?

#Now let's experiment with some if/else statements.
#Type in the code below.

birth_rate_mean = birth_rate.mean()
if birth_rate_mean > 100:
    print "The mean birth rate is greater than 100!"
else:
    print "The mean birth rate is not greater than 100!"

#What if we wanted to have more two options for this logical statement?
#Let's say we want to record whether the mean birth rate is between 0-10, 11-20, or >20.

if birth_rate_mean <= 10:
    print "The mean birth rate is between 0 and 10."
elif birth_rate_mean >= 11 and birth_rate_mean <= 20:
    print "The mean birth rate is between 11 and 20."
else:
    print "The mean birth rate is greater than 20."

#For the General Fertility Rate column, write a program that tells you if the standard deviation is:
# 0-15, 16-30, or >30.

#Now let's make what we call a list.

my_list = []

#Our list is empty. Let's add some stuff to it.

my_list.append(5)
my_list.append(6)
my_list.append(7)
print my_list

#We could also just make the list by doing this:

my_list = [5, 6, 7]

#Now that we've figured out how to make a list, let's introduce the concept of a loop.
#A loop will allow us to iterate over several items, e.g. numbers in our list!

my_new_list = []

for each_value in my_list:
    each_new_value = each_value * 5
    my_new_list.append(each_new_value)

print my_new_list

#In words, we have just told python to:
#1) create a new empty list called "my_new_list"
#2) for each value in our previously made list, create a new value titled each_new_value
#3) each_new_value will be the product of the my_list value and 5
#4) we will add these multiplied values to our new empty list

#On your own, try to make a loop that does the following:
#For each value in the "Birth Rate" column, if it is greater than 20, print "More babies!"
#If it is less than 20, print "Less babies!"

#I wonder if birth rate is related to fertility rate. Let's take a look at the data!
#Instead of using matplotlib's hist() function, we'll make a scatterplot.

import matplotlib.pyplot as plt

fertility_rate = health_data["General Fertility Rate"]

plt.scatter(fertility_rate, birth_rate)
plt.title("Birth Rate vs. Fertility Rate")
plt.ylabel("Birth Rate")
plt.xlabel("Fertility Rate")
plt.show()

#Nice! There seems to be a trend. Let's run a linear regression and plot the trend line.
#Here we'll use a module called "statsmodels" that will compute the statistics for us.

import statsmodels.api as sm
from statsmodels.api import add_constant

fertility_rate_reg = sm.add_constant(fertility_rate)
model = sm.OLS(birth_rate, fertility_rate_reg)
results = model.fit()
print results.params

#For every increase in fertility rate of 1, we get an increase of 0.1874 in birth rate!
#Our y-intercept is 2.8806.
#We can see if our results are significant by looking at the summary table.

##print results.summary()

#Are the results significant? 

#Now, plug in the values your found for slope and intercept below to plot a best fit line.
#We create a best fit line by using a for loop to multiply our fertility rate values by our calculated slope.

import matplotlib.pyplot as plt

slope = 0.1874
intercept = 2.8806
best_fit_line_values = []

for each_fertility_rate in fertility_rate:
    predicted_birth_rate = (each_fertility_rate * slope) + intercept
    best_fit_line_values.append(predicted_birth_rate)

plt.scatter(fertility_rate, birth_rate)
plt.title("Birth Rate vs. Fertility Rate")
plt.ylabel("Birth Rate")
plt.xlabel("Fertility Rate")
plt.plot(fertility_rate, best_fit_line_values)
plt.show()

#On your own, try to predict "Low Birth Weight" from "Prenatal Care Beginning in First Trimester" as the indepedent variable.
#Plot the results on a graph and report the slope, y-intercept, and p-value. 






