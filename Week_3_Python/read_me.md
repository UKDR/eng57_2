 start creating notes
 
 # Python basics
 
 #### Data Types in Python
 
##### Numeric
A numeric value is any representation of data which has a numeric value. Python identifies three types of numbers:

##### Integer: 

- Positive or negative whole numbers (without a fractional part)
- Float: Any real number with a floating point representation in which a fractional component is denoted by a decimal symbol or scientific notation
- Complex number: A number with a real and imaginary component represented as x+yj. x and y are floats and j is -1(square root of -1 called an imaginary number)

##### Boolean
Data with one of two built-in values True or False. Notice that 'T' and 'F' are capital. true and false are not valid booleans and Python will throw an error for them.

##### Sequence Type
A sequence is an ordered collection of similar or different data types. Python has the following built-in sequence data types:

- String: A string value is a collection of one or more characters put in single, double or triple quotes.
- List : A list object is an ordered collection of one or more data items, not necessarily of the same type, put in square brackets.
- Tuple: A Tuple object is an ordered collection of one or more data items, not necessarily of the same type, put in parentheses.

##### Dictionary
A dictionary object is an unordered collection of data in a key:value pair form. A collection of such pairs is enclosed in curly brackets. For example: {1:"Steve", 2:"Bill", 3:"Ram", 4: "Farha"}

##### type() function
Python has an in-built function type() to ascertain the data type of a certain value. For example, enter type(1234) in Python shell and it will return <class 'int'>, which means 1234 is an integer value. Try and verify the data type of different values in Python shell, as shown below.

````
>>> type(1234)
<class 'int'>
>>> type(55.50)
<class 'float'>
>>> type(6+4j)
<class 'complex'>
>>> type("hello")
<class 'str'>
>>> type([1,2,3,4])
<class 'list'>
>>> type((1,2,3,4))
<class 'tuple'>
>>> type({1:"one", 2:"two", 3:"three"})
<class 'dict'>

````
#### Creating Variables

Variables are containers for storing data values.

Example:
````
x = 5
y = "John"
print(x)
print(y)

````
Variables do not need to be declared with any particular type and can even change type after they have been set.
```
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)
```
String variables can be declared either by using single or double quotes:

```
x = "John"
# is the same as
x = 'John'
```
Another example:

```
one = 1
two = 2
three = one + two
print(three)
print(type(three))
```
#### Concatentaion or Formatiing?

Formatting:
```
print("What is your full name?")
my_name = input()
print("Nice to meet you {} ".format(my_name))
```

Concatenation:
```
print("What is your full name?")
my_name = input()
print("Nice to meet you " + my_name)

```
#### Types of Errors 

- **AssertionError**: 	Raised when an assert statement fails.
- **AttributeError**:	Raised when attribute assignment or reference fails.
- **EOFError**:	Raised when the input() function hits end-of-file condition.
- **FloatingPointError**: 	Raised when a floating point operation fails.
- **GeneratorExit**: 	Raise when a generator's close() method is called.
- **ImportError**: 	Raised when the imported module is not found.
- **IndexError**: 	Raised when the index of a sequence is out of range.
- **KeyError**: 	Raised when a key is not found in a dictionary.
- **KeyboardInterrupt**: 	Raised when the user hits the interrupt key (Ctrl+C or Delete).
- **MemoryError**: 	Raised when an operation runs out of memory.
- **NameError**: 	Raised when a variable is not found in local or global scope.
- **NotImplementedError**: 	Raised by abstract methods.
- **OSError**: 	Raised when system operation causes system related error.
- **OverflowError**: 	Raised when the result of an arithmetic operation is too large to be represented.
- **ReferenceError**: 	Raised when a weak reference proxy is used to access a garbage collected referent.
- **RuntimeError**: 	Raised when an error does not fall under any other category.
- **StopIteration**: 	Raised by next() function to indicate that there is no further item to be returned by iterator.
- **SyntaxError**: 	Raised by parser when syntax error is encountered.
- **IndentationError**: 	Raised when there is incorrect indentation.
- **TabError**: 	Raised when indentation consists of inconsistent tabs and spaces.
- **SystemError**: 	Raised when interpreter detects internal error.
- **SystemExit**: 	Raised by sys.exit() function.
- **TypeError**: 	Raised when a function or operation is applied to an object of incorrect type.
- **UnboundLocalError**: 	Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
- **UnicodeError**: 	Raised when a Unicode-related encoding or decoding error occurs.
- **UnicodeEncodeError**: 	Raised when a Unicode-related error occurs during encoding.
- **UnicodeDecodeError**: 	Raised when a Unicode-related error occurs during decoding.
- **UnicodeTranslateError**: 	Raised when a Unicode-related error occurs during translating.
- **ValueError**: 	Raised when a function gets an argument of correct type but improper value.
- **ZeroDivisionError**: 	Raised when the second operand of division or modulo operation is zero.
 