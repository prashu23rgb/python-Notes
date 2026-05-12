# this is how programming languages make decisions
# conditional statements are used to perform different actions based on different conditions. in python we have if, elif and else statements to make decisions in our code. 
lesson4 = "syntax of conditional statements in python"
first_input = input("enter a name ")

age = int(input("enter your age "))
"""
if age >=18:
    print(f"kya bolti company kamaya bahut money ? kahan hai teri naukari {first_input}" )
else: print(f"yaha kaise ? {first_input} ")
"""

 # notice the indentation in the above code. in python we use indentation to define the scope of a block of code. in this example the block of code that is executed when the condition age >= 18 is true is indented under the if statement. the block of code that is executed when the condition age >= 18 is false is indented under the else statement. indentation is very important in python because it defines the structure of the code and determines which block of code is executed based on the conditions.

'''NOTE - we used f string to print the value of the variable first_input in the string "kya bolti company kamaya bahut money ? kahan hai teri naukari {first_input}. 
f string is a way to format strings in python. we can use curly braces {} to enclose the variable name and it will be replaced with the value of the variable when the string is printed. '''

"""
if age >=18 and age < 100:
    print(f"kya bolti company kamaya bahut money ? kahan hai teri naukari {first_input}" )
elif age >=100:
    print ("is there wifi in hell?")
else :
    print(f"yaha kaise ? {first_input} ")"""

# NOTE -  now we have used elif statement to check for another condition when the age is greater than or equal to 100. if the age is greater than or equal to 100 then it will print "is there wifi in hell?" otherwise it will print "yaha kaise ? {first_input}" when the age is less than 18 . elif  statement (elseif) is used to check for multiple conditions in our code. we can have as many elif statements as we want in our code. the elif statement is executed when the condition in the if statement is false and the condition in the elif statement is true. if all the conditions in the if and elif statements are false then the else statement is executed.

# what is nested if statement ?
# nested if statement is an if statement that is inside another if statement. we can use nested 

# driving license checking program using nested if statement
"""
if age <18  :
    print(f"tu abhi bhi yahi hai {first_input} ")

else:
    if age >100:
     print("budhaape mein gaadi chalaane ka shauk hai kya ?")
    else:
        experience = input("DO you have any driving experience? (y/n) ")
        if experience != "y" and experience != "n":
            print("please enter valid input for experience (y/n)")
        elif experience == "y":
            print(f"congratulations {first_input} your driving licence will be issued soon")
        else:
            print(f"please schedule an appointment  {first_input} ")"""
            
""" i know this code is not perfect but it is just an example to show how we can use nested if statements in python. we can also use elif statements to check for multiple conditions instead of using nested if statements. for example we can rewrite the above code using elif statements as follows:"""
'''

if age <18  :
    print(f"tu abhi bhi yahi hai {first_input} ")
elif age >100:
     print("budhaape mein gaadi chalaane ka shauk hai kya ?")   
else:
    experience = input("DO you have any driving experience? (y/n) ")
    if experience != "y" and experience != "n":
        print("please enter valid input for experience (y/n)")
    elif experience == "y":
        print(f"congratulations {first_input} your driving licence will be issued soon")
    else:
        print(f"please schedule an appointment  {first_input} ")
        '''
        
# RULE 1:
# Every condition statement must end with a colon (:)

if True:
    pass


# RULE 2:
# Indentation is mandatory in Python
# Python uses indentation to define code blocks

if True:
    print("inside if block")
else:
    print("outside if block")



# RULE 4:
# else never takes a condition

# CORRECT ✅
'''else:
    pass'''

# WRONG ❌
# else condition:


# RULE 5:
# Multiple elif statements are allowed
'''
if condition1:
    pass

elif condition2:
    pass

elif condition3:
    pass

elif condition4:
    pass

else:
    pass
'''

"""lets understand comparison operators in python with the help of a program to check the temperature to play cricket or not
COMPARISON OPERATORS

These create boolean results.

Operator	
==	equal  NOTE -  in programming = is a asingment operator that is use to aasign a value to a variable 

==  is a comparion operator that is used to compare two values and it returns true if the values are equal and false if the values are not equal. 

!=	not equal
>	greater
<	smaller
>=	greater/equal
<=	smaller/equal

"""



#lets make a program to check the temperature to play cricket or not
"""
if tem > 40 ------- too hot to play cricket
if temp >0 and temp < 20 ------ too cold to play cricket
if tem > 100 -------- are you still alive ?
if tem < 0 --------- you are a yeti living in ice age 
if tem < 40 and tem > 20 ------- perfect for playing cricket

"""
temp = int (input("enter the temperature in degree celsius "))

'''if temp > 100:
    print("are you still alive ?")
elif temp <=100 and temp>= 40:
    print("too hot to play cricket")
elif temp <=40 and temp >= 20:
    print("perfect for playing cricket")
elif temp < 20 and temp > 0:
    print("too cold to play cricket")
else:
    print("you are a yeti living in ice age ")'''
    
    
# we can write the above code in a more concise way using logical operators as follows:
if temp > 100:
    print("are you still alive ?")
elif 40 <= temp <= 100:
    print("too hot to play cricket")
elif 20<= temp < 40:
    print("perfect for playing cricket")
elif 0 <=temp < 20:
    print("too cold to play cricket")
else:
    print("you are a yeti living in ice age ")