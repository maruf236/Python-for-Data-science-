s= ' string '# 'it's raining outside '
# to solve it, use "It's raining outside"
s="string"
# For multiline strings need to use """ """  
s='''Hello'''
s=""" Hello """
# type conversion 
s= str('Hello')
print(s)


# Accessing Substring from a String

# Positive indexing 
s='Hello World '
print (s[0])
print (s[1])
#  print (s[41])   # Error 

# Negative indexing 

S= "hello World"
print (S[-1])
print (S[-2])
print (S[-3])


# Slicing 
S = 'Hello world'

print (s[2:7]) # starting index is 3 and ending index is 
# 4 but the ending index is excluded . so need to add 1 with 
# ending index 
# so print(s[starting index : ending index +1 ])
print (s[0:5])
print (s[2:3])
print (s[2:]) # Ending index skip means -> starting index to ending automatically 
print (s[:3])  # Starting number skip means starting to given ending number-1 

#Step slicing 

# Positive indexing 
print (s[0: :2]) # Loop system 
# Starting iteration: Ending iteration : stepping 
print (s[0: :3])
# Negative indexing 
print (s[-1: :-2])
# String reversing 
print (s[::-1])
print (s[-6:])
print (s[-6:-1])
print (s[-1:-7:-1])


# Editing and Deleting in string 
s='hello world'
#s[0]='H' # 'Str' object does not support item assignment . 
         # likw other language c /c++
         # we cannot cahnge it . Fixed. 
# Python strings are immutable . not like virus DNA (Hahah....)

# del for delete 
del s 
print (s)

s= 'hello world '
del s[-1:-5:2]
print (s)