# Define
# the
# following
# variables
# name, last_name, age, eye_color, hair_color
# name = ''
# last_name = ''
# eye_color = ''
# hair_color = ''
# age = ''
# Prompt user for input and Re-assign these

# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.

# Extra:
# Section 2 - Calculate in what year was the person born? and responde back.
# print something like: 'You said you we're 28 hence you were born in 1991!'

# Extra - Cast your input
#
# name = input("What is your full name?  ")
# age = input("How old are you?   ")
# #  = input("What's your date of birth? ")

# We can choose between concatenation or format
def all():
    print("What is your full name?")
    my_name = input()
    print("Nice to meet you {} ".format(my_name))
    print("What is your eye colour?")
    eye_colour = input()
    print("Wow! I'm jealous, I wish I had eyes.")
    print("What about your hair colour " + my_name + "?")
    hair_colour = input()
    print("That's Awesome! I have green hair...I think.")
    print("So, " + my_name + " what is your favourite food?")
    favourite_food = input()
    print("Ah, your favourite food is {} - mine too!".format(favourite_food))
    print("mmm... " + my_name + ", Which year were you born (yyyy)? ")
    age = int(input())
    DOB = int(2020)
    age_now = str(DOB - age)
    print("Wow... which means you either are or going to be " + age_now + " this year, right?")
    yes_no = input()
    print("Well {}, you don't look a day over 20!".format(my_name))

all()

# Function Simplified

def my_ai():
    name = input("What is your name? ")
    print("Nice to meet you {} ".format(name))
    eyes = input("What is your eye colour? ")
    print("Wow! I'm jealous, I wish I had eyes.")
    hair = input("What about your hair colour {}? ".format(name))
    print("That's Awesome! I have green hair...I think.")
    year = int(input("mmm...{}, which year were you born (yyyy)? ".format(name)))
    birth = int(2020)
    age_current = str(birth - year)
    yea_no = input("Wow... which means you either are or going to be {} this year, right? " .format(age_current))
    print("Well {}, you don't look a day over 20!".format(name))

my_ai()
