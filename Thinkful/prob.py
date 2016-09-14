prob.py

import collections

testlist = [1, 4, 5, 6, 9, 9, 9]

c = collections.Counter(testlist)

print(c)

# calculate the number of instances in the list
count_sum = sum(c.values())

for k,v in c.iteritems():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))


# generate box plot
import matplotlib.pyplot as plt
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.boxplot(x)
plt.show()
# save box plot, histogram, and QQ plot
plt.savefig("boxplot.png")


# generate histogram
plt.hist(x, histtype='bar')
plt.show()

# save histogram
plt.savefig("histogram.png")


# generate QQ plot
import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.figure()
test_data = np.random.normal(size=1000)   
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show() #this will generate the first graph
plt.figure()
test_data2 = np.random.uniform(size=1000)   
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show() #this will generate the second graph

# save QQ plot
plt.savefig("qqplot.png")

