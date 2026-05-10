#lets start from printing otuput on the screen
print("hello guys this is my github repository")

LESSON1 = "VARIABLE IN PYTHON"
 
'''lets learn about variables in python. a variable is a container that holds a value. we can assign a value to a variable using the assignment operator (=). we can also change the value of a variable by reassigning it. in this example we will create a variable called name and assign it a value of "priyanshu". we will then print the value of the variable on the screen.'''

name = "priyanshu"
# using " " beacause it is a string data type

''' NOTE = variable is a name reference to a memory location that stores a value.
priyanshu - value  {value can be any data type such as string, integer, float, etc. in this example it is a string data type.}
name - variable name which is a reference to the value priyanshu in memory.
'''

print ("my name is " + name); # note that ; is not required in python but it is used to separate multiple statements on a single line. in this example we have only one statement so we can omit the ;. + is used to concatenate two strings. in this example we are concatenating the string "my name is " with the value of the variable name.

a,b,c= 1,"priyanshu",3.14 
# we can also assign multiple values to multiple variables in a single line. in this example we have assigned the value 1 to variable a, "priyanshu" to variable b and 3.14 to variable c.
print(f"hii my name is {name} i wanna be in number {a} in coding unique as value of pie {c}")
# we can also use f-strings to print the value of a variable in a string. f-strings are a way to format strings in python. we can use curly braces {} to enclose the variable name and it will be replaced with the value of the variable when the string is printed.

#we can also use single quotes (' ') to define a string variable. for example:

name = 'priyanshu'
print(name)


# state - programming is mostly about changing the state of a program. state is the current condition or status of a program.
score = 0 # old state where score is 0
score= score + 10 # new state where score is 10. we have changed the state of the program by updating the value of the variable score. we can also use the shorthand operator += to update the value of a variable. for example:
score += 10 # this is equivalent to score = score + 10 NOTE : NOW THE VALUE OF SCORE IS 20 BECAUSE WE HAVE UPDATED IT TWICE. FIRST TIME WE UPDATED IT TO 10 AND THEN WE UPDATED IT TO 20. NOW THE VALUE OF SCORE IS 20.
print(score)

LESSON2 = "VARIABLE TYPES OF OPERATIONS"

# ASSINGMENT OPERATOR (=) - used to assign a value to a variable. for example:
X = 20
# REASSINGMENT OPERATOR (+=, -=, *=, /=) - used to update the value of a variable. for example:
X = 24 ; X +=4 # x= x + 4
print(X)  
# increment operator (++) - used to increase the value of a variable by 1 in c , c++  and java but in python we can use the shorthand operator += to achieve the same result. for example:
# X = X ++ error because ++ is not a valid operator in python. we can use X += 1 to increment the value of X by 1. for example:
X += 1 # this is equivalent to X = X + 1
print(X) # now the value of X is 29 because we have updated it three times. first time we updated it to 24, then we updated it to 28 and then we updated it to 29.

# swaqpping - we can swap the values of two variables without using a temporary variable. for example:
a = 10
b = 20
a, b = b, a # this is a pythonic way to swap the values of two variables without using a temporary variable. in this example we are swapping the values of a and b. after this statement the value of a will be 20 and the value of b will be 10.
print (a,b)


LESSON3 = "DATA TYPES IN PYTHON"
# list of all the data types in python:
# 1. integer - used to represent whole numbers. for example: 1,
integer = int(10) #or  integer = 10
#float - used to represent decimal numbers. for example: 3.14,
float = float(3.14 ) #or float = 3.14
# string - used to represent text. for example: "priyanshu",
string = str("priyanshu ") #or string = "priyanshu"
# boolean - used to represent true or false values. for example: True, False
boolean = bool(True) #or boolean = True 
BOOLEAN = bool(1) # in python we can also use 1 and 0 to represent true and false values respectively.
Boolean, BoolEAN = bool(5), bool(0) # in python any non-zero value is considered as true and zero is considered as false. so in this example the value of Boolean is 5 which is a non-zero value so it is considered as true.

# NOTE  python is a case sensitive language. so we can use uppercase and lowercase letters to define variables. for example:
print (BOOLEAN, Boolean, boolean, BoolEAN) 

# now we will understand some complex data types in python such as list, tuple, set and dictionary.

list = [1, 2, 3, 4, 5, 5, 5 , 5] # list is a collection of items which is ordered and changeable. it allows duplicate members.
tuple = (1, 2, 3, 4, 5) # tuple is a collection of items which is ordered and unchangeable. it allows duplicate members.
set = {1, 2, 3, 4, 5} # set is a collection of items which is unordered and unindexed. it does not allow duplicate members.
dictionary = {"name": "priyanshu", "age": 20, "city": "delhi"} # dictionary is a collection of items which is unordered, changeable and indexed. it does not allow duplicate members. it consists of key-value pairs. in this example the key is "name" and the value is "priyanshu". the key is "age" and the value is 20. the key is "city" and the value is "delhi".

