import matplotlib.pyplot as plt

#x is the amount of pie
#y is the labels

labels = 'Taxes', 'Overhead', 'Entertainment'
sizes = [25, 32, 12]
colors = ['c','m','b']

plt.pie(sizes, labels=labels, colors=colors, startangle=90, explode=(0,0.1,0), autopct='%1.1f%%', shadow=True)
plt.axis('equal') #keeps it undistorted
plt.show()
