#swap two numbers


a=(int(input("Enter a value")))
b=(int(input("enter b value")))

print("A and B values before swapping:")
print("a = ",a)
print("b = ",b)

a,b = b,a
print("A and B values after swapping:")
print("a = ",a)
print("b = ",b)