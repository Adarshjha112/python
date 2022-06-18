
#single dimensional array

import numpy as np
n1 = np.array([1,2,30])
print(n1)

#Multi dimensional array
n2 = np.array([[1,2,3],[5,6,7]])
print(n2)
type(n2)

#numpy array with same number
n3 = np.full((2,2),10)
print(n3)

#numpy array within a range
n4 = np.arange(10,20)  # last element is exclusive
print(n4)

#numpy array within a range with gap of 5
n5 = np.arange(10,50,5)
print(n5)


#numpy with random numbers between 1 to 100
n6 = np.random.randint(1,100,5)
print(n6)

#shape of array

print(n6.shape)

#joining two numpy arrays using v stack and h stack
n8 = np.array([10,20,30])
n9 = np.array([40,50,60])
np.vstack((n8,n9))
print(np.vstack((n8,n9)))

#Addition  ---axis = 0 colomn wise and axis = 1 row wise
n11 = np.array([1,2,3])
n10 = np.array([2,3,4])
print(np.sum([n11,n10],axis=1))

#subtraction

n10 = n10-1
print(n10)

#multiple
n10 = n10*2
print(n10)

#numpy math function
#mean
n17 = np.array([1,2,3])
print(np.mean(n17))
#median
print(np.median(n17))

#standard deviation
print(np.std(n17))











