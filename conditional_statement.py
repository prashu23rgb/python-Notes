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