#matlpotlib

#line plot
import numpy as np

from matplotlib import pyplot as plt
x= np.arange(1,11)
print(x)

y = 2*x
print(y)

plt.plot(x,y , color ='r')  #with color red
#plt.show()

#for title and lable use or add

plt.title("Line plot")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.show()

#using scatter plot
plt.scatter(x,y)
plt.title("scatter plot")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.show()

#numerical value use for histogram chart and categorical value use for bar chart

#histogram plot
plt.hist(x,y)
plt.title("histogram plot")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.show()





