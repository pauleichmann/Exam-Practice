'''
PlotQuestion.py

See the README for the full description of the desired plot.


TOTAL POINTS AVAILABLE: 10 

10 points - desired plot is generated and code is efficient 

6-9 points - desired plot is generated, but code could be 
improved (e.g., the students used unnecessary if statements)

4-6 points - plot is generated but it has some errors

1-4 points - no plot is generated, but some effort was made to generate one

0 points - no effort made to answer question





'''
# Write a Python script that reads in the text file `data.txt`, in the folder Data, and generates 
# one plot as shown in image.png
# 
# Read the text file (hint: the delimiter in the 
# file is `','`) and notice that there are 9 columns. The first column represents the time of the 
# measurement, whereas the other columns represent data collected 
# at that specific time. To get maximum marks you need to be sure that the code you write can be executed on a computer different than yours (meaning, do not use
# absolute paths when opening and closing directories).
# 
# - Plot the data contained in the 6th column against the data contained in the 1st column (i.e., 
#   data in the 6th column on the y axis, data in the 1st column on the x axis). 
# - Plot the data contained in the 3rd column against the data contained in the 1st column (i.e., 
#   data in the 3rd column on the y axis, data in the 1st column on the x axis). 
# - Add an xlabel as "Time [s]" and a ylabel as "Speed [m/s]"
#

import matplotlib.pyplot as plt 
import numpy as np 
import os

os.chdir("Plot question")
os.chdir("Data")

with open("data.txt", "r") as file: 
    data = file.readlines()

length = len(data)

dataList = []

for i in range(length):
    line = data[i]
    splitline = line.split()
    dataList.append(splitline)

dataArray = np.array(dataList)

time = []
thirdColoum = []
sixthColoum = []

for line in dataArray:
    time.append(line[0])
    thirdColoum.append(line[2])
    sixthColoum.append(line[5])

timearray = np.array(time)
trdColArray = np.array(thirdColoum)
sixColArray = np.array(sixthColoum)

plt.plot(timearray,trdColArray, "r")
plt.plot(timearray, sixColArray, "b") 

plt.xlabel("Time [s]")
plt.ylabel("Speed [m/s]")
plt.show()