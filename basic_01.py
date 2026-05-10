#lets start from printing otuput on the screen
print("hello guys this is my github repository")

'''lets learn about variables in python. a variable is a container that holds a value. we can assign a value to a variable using the assignment operator (=). we can also change the value of a variable by reassigning it. in this example we will create a variable called name and assign it a value of "priyanshu". we will then print the value of the variable on the screen.'''

name = "priyanshu"
# using " " beacause it is a string data type

print ("my name is " + name); # note that ; is not required in python but it is used to separate multiple statements on a single line. in this example we have only one statement so we can omit the ;. + is used to concatenate two strings. in this example we are concatenating the string "my name is " with the value of the variable name.

a,b,c= 1,"priyanshu",3.14 
# we can also assign multiple values to multiple variables in a single line. in this example we have assigned the value 1 to variable a, "priyanshu" to variable b and 3.14 to variable c.
print(f"hii my name is {name} i wanna be in number {a} in coding unique as value of pie {c}")
# we can also use f-strings to print the value of a variable in a string. f-strings are a way to format strings in python. we can use curly braces {} to enclose the variable name and it will be replaced with the value of the variable when the string is printed.

#we can also use single quotes (' ') to define a string variable. for example:

name = 'priyanshu'
print(name)


# lets create a function to add two numbers fuction is a block of code which performs a specific task and can be reused in the program. we can define a function using the def keyword followed by the function name and parentheses. we can also pass parameters to the function which are used to perform the task. in this example we will create a function to add two numbers and return the result.
def add(a,b):
    return a+b
print(add(2,3))

