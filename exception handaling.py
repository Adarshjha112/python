#The try block lets you test a block of code for errors.

#The except block lets you handle the error.

#The else block lets you execute code when there is no error.

#The finally block lets you execute code, regardless of the result of the try- and except blocks.






#The try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")

#if error in try print except
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

#print try statements with else  because of no error in try .
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


#finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
