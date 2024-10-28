"""Variables
Variables are containers for storing data values."""

# Rules for variable create 

# can't start first letter numbers  and special charchater 
# case sentitive 
# 
"""
Variable Names:
--------------
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
-->A variable name must start with a letter or the underscore character
-->A variable name cannot start with a number
-->A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
-->Variable names are case-sensitive (age, Age and AGE are three different variables)
-->A variable name cannot be any of the Python keywords.



"""
# import keyword
# print(keyword.kwlist)


# Data Types :
"""
text ---> string (str)
whole number --> interger (int)
point number --> float 
boolen values --> bool(True,False)
None type--> None
number+str--> complex 
"""

# temp="hi ,bye" #int,float ,complex,None
# print(temp,type(temp))


"""

Python Type Conversion
In programming, type conversion is the process of converting data of one type to another. For example: converting int data to str.

There are two types of type conversion in Python.

Implicit Conversion - automatic type conversion
Explicit Conversion - manual type conversion


"""
#Implicit Conversion - automatic type conversion


# a=10.78
# print(a,type(a))


# #Explicit Conversion - manual type conversion
# age=float(99) #
# print(age,type(age))


# name=int('sanjay') #error
# print(name)


salary=10000 # int
print(float(salary),salary)

s=int(False)
print(s)


# str--> int , float,complex
# int--> float, complex, str
# float--> int , str,complex

s=complex(44.7)
print(s)

















