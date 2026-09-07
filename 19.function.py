# What is function ? 
# It is a programming construct that return output if i give some input.
# 2 types--
# Built in function -- print(), type(),input().
# user define  -- user desired function .
# 
# Abstruction -- Have someting but not visible.
# Decomposition -- Multiple function working to built the system. 
# 
# Component of function --
# def keyword -- means function 
# def ---Name_of_function (input):
#  """Docs string-reading manual"""
# line of code
#  return output 
# the n do amke a call of the function #


# Function creation   __ Inputed place call parameter during creation 
def odd_even(number):
    """
    It's check the given number is odd or even. 
    input - any valid integer .
    output- odd/even.
    created on - 3rd sep 2026
    """
    if type(number)== int :
        if number %2==0:
            return "even"
        else:
            return "odd"
    else : return "Are you mad ?"
# Function call -- Function_name(input)-- Inputed place call argument during insertion.

for i in range (1,11):
    x=odd_even(i)
    print (x)

print(odd_even("hello"))


# There is 2 point of view - 1) Creating a function 2) Using a function

# Types of arguments 
#    * Default Argument -- 
#    * Positional Argument --  
#    * Keyword Argument -- 

# Default Argument -- A default argument is a value that is automatically used 
# by a function if the user does not provide a value for that parameter.

def power(a=1,b=1):    # If the value of a/b not given the assume then the value will be 1    
    return a**b

print (power (2,3))     # 8
print (power(2))        # 2 
print (power())         # 1

# Positional argument -- A positional argument is an argument that is passed to a function based 
# on its position (order) 

print(power(2,3))   # the order send value by the argument the same way the parameter receive it.


# Keyword Argument --  at this point the parameter ius called keyword
print (power (b=3,a=2)) # position doesnot matter,just want the value of a and b to the right parameter
                        # Good for multiple parameter.


# *args and **kwargs -- are special Python keyword that are used to pass the variable length of arguments to a function.

# *args 
# allows us to pass a variable number of non-keyword arguments to a function.


# Here if we want to multiply once 2 variable next 10 varibles then we need to recreate the function but using the 
# args it's not necessary.
def multiply (a,b,c,d):
    return a*b*c*d

print(multiply (7,9,5,4))

def argsmultiply(*args):
    product =1
    for i in args:               # If the value range is known then use range otherwise use the variable
        product= product*i
    print (args)                  # tuple
    return product 
print (argsmultiply(1,2,3,4,5,6,7,1,2,3,3,0))   # Mulitiple value inputed but calculated easily without recreat the function.


def argadd(*sarwar):
    result =0
    for i in sarwar:
        result += i
    print (sarwar)
    return result

print ( argadd(1,2,3,4,5,6,7))






