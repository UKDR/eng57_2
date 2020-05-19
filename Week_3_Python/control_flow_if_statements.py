import time
# Control Flow

# control flow dictates where the code will run.
# Similar to dams in real life
# in coding we do this with < if functions and while loops.

# if functions
# if functions work with booleans (True or False)
# we usually use comparison operators to equate and compare objects and result in true or false Booleans

# syntax if function
# if <condition>:
#   block of code
#   block is a set of code that runs
#   in python, block is defined by indentation
# elif <second_condition>:
#   run this block of code
# else:
#   block of code

#logical AND
# syntax
# <condition> and <condition>
# both sides need to result in true to be true
print(True and True) # ans: true
print(True and False) # ans: false

#logical OR
# syntax
# <condition> and <condition>
# only one side needs to be true, to result in true
print(True or True) # ans : true
print(True or False) # ans: true



weather = input("What is the weather today?     ")
#weather = "stormy"
safety_alert = "red"

# if true - either works
if weather == "rainy":
    #time.sleep(2)
    print("bring umbrella")
elif weather == "stormy" and safety_alert == "red":
    print('duck for cover')
elif weather == "stormy":
    print("Amazon prime & chill at home")
else:
    print("bring suncream")

# if you always want to make or case a function
# if <condition>:
#     print("this was true")
# if <condition>:
#     print("this was true")
# if <condition>:
#     print("this was true")