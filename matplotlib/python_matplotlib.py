#3rd party but one of the most used
#data visualization module
import matplotlib.pyplot as plt

#line graph
x = [1, 2, 3, 4, 5]
y = [4, 5, 6, 7, 3]
y2 = [6, 3, 1, 6, 8]
plt.plot(x, y, label='initial line') #plot method, draws in the background, at the very end, will bring it to the screen to user
plt.plot(x, y2, label='new line')
plt.xlabel('Plot Number')
plt.ylabel('Random Number')
plt.title('Epic graph')
plt.legend() #can change the position and so on
plt.show() #script will pause until save/close the figure that pops up

#bar chart
m = [1, 2, 3, 4, 5]
n = [4, 5, 6, 7, 3]
n2 = [6, 3, 1, 6, 8]
''' but will overlap!
plt.bar(m,n, label='chart1', color='g')
plt.bar(m,n2, label='chart2', color='m')
'''
plt.legend() #can change the position and so on
plt.show() #script will pause until save/close the figure that pops up

#histogram
test_scores = [55,67,43,89,99,87,65,90,32,33,44,67,78,65,44,88,54,99,77,88,78,83,83,93,70]
x = [x for x in range(len(test_scores))] #will make a bunch of x: it's simply the student id and the score they got
plt.bar(x, test_scores)
plt.show()

#shows the frequency of students who got a score in a certain range:
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] #possible bins
plt.hist(test_scores, bins, histtype='bar', rwidth=0.8) #put the scores in the bins
plt.show()
#can use cumulative=True

#scatter plots
test_scores2 = [55,67,43,89,99,87,65,90,32,33,44,67,78,65,44,88,54,99,77,88,78,83,83,93,70]
time_spent =   [33,11,23,34,45,50,34,32,54,55,43,23,53,33,23,55,23,33,27,45,56,52,40,50,51]
plt.scatter(time_spent, test_scores)
plt.xlabel('time spent on test')
plt.ylabel('test score')
plt.show()
