import matplotlib.pyplot as plt
import csv
#-------how to read a csv with csv module--------------
x = []
y = []
#example.txt has x,y on each row
with open('example.txt') as csvfile:
    plots = csv.reader(csvfile, delimiter=',') #reads the csv file
    for row in plots:
        x.append(int(row[0])) #populates the above x=[]
        y.append(int(row[1]))

plt.plot(x,y, label='Loaded from file')
plt.xlabel=('plot number')
plt.ylabel=('randomly chosen number')
plt.show()

#------------using numpy to load the data instead (faster than the csv module)--
import numpy as np

m, n = np.loadtxt('example.txt',delimiter=',', unpack=True) #unpacking assigns 1 value to m and next to n

plt.plot(m,n, label='Loaded from file')
plt.xlabel=('plot number')
plt.ylabel=('randomly chosen number')
plt.show()
