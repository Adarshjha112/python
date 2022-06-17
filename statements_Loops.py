#if statement

a=10
b=20
if b>a :
    print("b is greater")
else :
    print("a is greater")

#elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

  #Loops
i = 1
while i<= 10:
    print(i)
    i =i+1

L1 =['mango','apple','orange']

for i in L1:
    print(i)

L1 = ['mango', 'apple', 'orange']
L2 =['chair','book','laptop']
for i in L1:
    for j in L2:
        print(i,j)