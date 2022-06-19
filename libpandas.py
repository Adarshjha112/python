#pandas series object is one dimensional array
#Series s in capital
#install package pandas
import pandas as pd

s1 = pd.Series([1,2,3])
print(s1)

#changing indexs
s2 = pd.Series([1,2,3], index = ['a','b','c'])
print(s2)


#extracting a single element
L1 =([1,2,3,4,5,6])
s4 = pd.Series(L1)
print(s4[3])
#sequence of number upto 4
print(s4[:4])

#add two series objects

L3 = pd.Series([1,2,3])
L4 = pd.Series([4,5,6])
#s6 = sum(L3,L4)
s5 = L3+L4
print(s5)
#print(s6)

#Dataframe - two dimensional ,comprises of rows and columns
import pandas as pd
s8 = pd.DataFrame({"Name ": ['ram','kyuu'] , "marks":[23,32]})
print(s8)




