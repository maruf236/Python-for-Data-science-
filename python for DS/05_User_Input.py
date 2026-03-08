#User input 

#In the world has just two type of software 
#   1. Static -> Don't talk with user (calendar)
#   2. Dynamic -> talk with the user like calculator

#Take input from users and store them in a variable
input('Enter your name :')  

#input -> Universal data format that can store anything as string 

a = input('Enter 1st number : ')
b = input('Enter 2nd Number : ')

print(type(a), type(b))

#Add the variable and store 
c = a + b   # String concatenation happens

#print the result 
print(c)    # Printed result is string so need type conversion 

#Type conversion

#1. Implicit: The interpreter does the conversion automatically
#print(5 + 5.6) # handdle by interpreter 
#print(type(5), type(5.6)) # Int , float 
#print(type(5), type('5.6')) # Int , str
# ^ cannot handdle by interpreter. so need Explicit.

#2. Explicit: 
#       Built in function:
#         str->int : int ('44.5','3') output : 44,3 
#         int (4+5j) : error so impossible  
#         str-('3') : output 3 
#         float (4) : output 4.00
a=int (a)
b=int (b)
#a and b originally changes to int
c=a+b
print (c) #output is int 
print (a*b)

# Python type convertion operation doesnot changes the original data
