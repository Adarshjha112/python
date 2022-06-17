#function
from functools import reduce


def hello():

    print("hello")
hello()

def odd_even(x):
    if x%2==0:
        print(x,"is even")
    else:
        print(x,'is odd')
odd_even(2)


#lambda function
g = lambda x: x*x*x
print(g)
g(10)

#filter /map/reduce in lambda
L1 = [87,56,90]
final_list = list(filter(lambda x: (x%2!=0),L1))
print(final_list)

L2 =[1,2,3]
list_final=list(map(lambda x:x*2,L2))
print(list_final)

sum =reduce(lambda x,y:x+y,L2)

print(sum)
