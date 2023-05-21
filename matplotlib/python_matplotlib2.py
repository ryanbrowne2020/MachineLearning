import matplotlib.pyplot as plt
#stack plot
year = [1,2,3,4,5,6,7,8,9,10]
#in the thousands
taxes = [17,18,43,40,8,43,42,39,30,32]
overheads = [30,22,9,29,17,12,14,24,49,35]
entertainment = [41,32,27,13,19,12,22,18,28,20]

plt.plot([],[], color='m', label='taxes') #can plot empty to make a label for the stackplot
plt.plot([],[], color='c', label='overheads')
plt.plot([],[], color='b', label='entertainment')
plt.stackplot(year, taxes, overheads, entertainment, colors=['m','c','b'])
plt.legend()
plt.show()
