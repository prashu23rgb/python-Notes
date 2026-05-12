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