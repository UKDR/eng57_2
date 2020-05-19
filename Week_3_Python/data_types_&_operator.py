# Data Types & Operator

# string_fixed = ' I said \'Wow!\''
# the above statement is the same as using Double quotes inside single

# slicing strings

# h e l l o ! w o r l d
# 0 1 2 3 4 5 6 7 8 9 10

hw = "Hello! World"
print(hw[7:]) # checks the 7th string and onwards
print(hw[0:5]) # looks at the string between 0 - 5
print(len(hw)) # counts how long the string is

# strip
white_space = "lot's of space at the end    "
print(len(white_space)) # counts how long the white_space string is

print(len(white_space.strip())) # strip gets rid of empty spaces at the end of the line

# some more methods sub-string
example_text = "some Text here"
print(example_text.count("here")) # count shows how many times the text appears in the sentence

print(example_text.lower()) # changes all the text to lower case
print(example_text.upper()) # changes all the text to UPPER case

print(example_text.capitalize()) # capitalises the first letter in the sentence

print(example_text.replace("some", "plenty")) # replaces the chosen word with another word

# Concatenation & Casting
x = 2  # Integer
y = 5.4  # Float
z = "I am"

str(x) # changing integer to string
str(y) # changing integer to string
print(z + " " + str(y) + " " + str(x)) # concatentating integers and strings together

x = "6"
print(int(x)) # converts to integer
print(float(x)) # converts into float
print(type(x)) # finds the type of variable

# Boolean operators
a = True
b = False
c = 2
d = 1
# == The two equal sign checks if they are equal to each other
# != checks if they are not equal to each other

greet = "Hello World!"
print(greet.startswith("H")) # checks if the string starts with H
print(greet.endswith("!")) # checks if the string ends in !
print("" == None) # the empty space is a string and None is nothing, False, they are different











