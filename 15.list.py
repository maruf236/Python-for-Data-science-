# List  -  Same as structure of C++ 

# what is list? 
# list vs Array
# Character of a List
# How to creat a list
# Access items from a list
# Editing item in a list
# Deleting item from a list
# Operation On list
# Function on List
# 
# 
# List is a datatype where we can store multiple item under 
# 1 name. 
# we can store multiple things in a list .
# L=[20,'jessa',35.54,[30,60,70]]
# 
# 
# List like array . but have some differences . 
#                 Array vs List 
# * Fixed size (need to declear) vs Dynamic Size (not declear )
# * Convenience (homogenous single datatype ) -> Hetrogeneous (Multiple datatype )
# * Speed of Execution less for List but array is speedy 
# * memory occupied more for List but less for Array 
# 
# how to store list in memory ?
# Array-> int arr[50] -> continuous memory block to store int to  binary form  .
# but list store in  different memory address but store the address in list. 
# List another name is referencial array.
# List is Dynamic Array. Unlimited value can store.

# How a list can store multiple type of datatype  easily?
# why list name is referencila array ?
# id()-> print the memory address.

l=[1,2,3]
print(l)          #[1, 2, 3]
print(id(l))      #888
print(id(l[0]))   #960 
print(id(l[1]))   #992
print(id(l[2]))   #024
print(id(1))      #960
print(id(2))      #992
print(id(3))      #024

# Characteristics of List
# Ordered Matter 
# Changeble/Mutable  
# Heterogenous - add multiple different type of datatype 
# can have duplicate - 1,2,2,3,3....
# are dynamic - 
# can be nested - 
# items can be accessed - 
# can contain any kind of objects in python 


# Creating a List
#  
# Empty----1D----2D----3D----Hetrogenous----Using type converstion
# 
print([])                        #  Empty list
print([1,2,3,4,5])               #  1D list- Homo
print ([1,2,3,4,[1,2,3,4,5]])    #  2D list- Hetrogenous - cause integer and list
print([[[1,2],[3,4]],[[1,2],[3,4]]])  #3D list - Homogenous list
print([1,2,3,5.3,5+6J])          # hetrogenous list
print(list('hello'))    # list keyword - make the given things to list

# Accessing items from list
# Indexing -Positive and Negative
l=[1,2,3,4,5]    # 1D
print (l[0])      # Goes from left to right and start with 0
print (l[-1])     # Goes right to left and start with -1 

l=[1,2,3,4,5,[1,2,3]]    # 2D
print(l[-1][0])
print(l[-1][-2])
print(l[-1][-1])

l=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12,]]]    #3D
print(l[0])    # -> First enter to list 1 
print(l[0][0])  # -> First enter to list 1 (among two) then in 1( among two) 
print(l[0][0][1]) # -> First enter to list 1 (among two ) then in 1 ( among two) then also in 2nd number ( among three) 
print(l[1][1][2])    # 1->1->2

# Slicing  ( part of the list  extract)
l= [1,2,3,4,5,6]
print(l[0:3])
print(l[0: :2])  # stepping included 2
print(l[-5:-2:2])
print(l[ : :-1])    # Reversing 

# Adding items to a list 
# Append -- Extend --Insert
# Append -- add one item at a time 
l=[1,2,3,4,5]
l.append(6)
print (l)
l.append([9,10,11]) # No problem - added but as a list in the list  not as a single item 
print(l)
# Extend --  Add multiple item at a time 
l.extend([6,7,8])  # This added as a item not as a list 
print (l)
l.extend('dhaka')  # Added the 'dhaka''s all letter as letter to the list no as string .
print(l)
# Insert -- add item a certain index 
l.insert(1,100)  # Index no and the number ( index, number )
print(l)
l.insert(3,l.extend([200,300]))  # not added the given iondex add to the last of the list.
print (l)


# Editing of the list --- List is mutable 
l= [1,2,3,4,5]
l[-1]=500
print(l) 

# editing with slicing 
l[1:4]=[100,200,300]
print (l)

# Deleting items from a list
# del -- remove -- Pop -- clear 

# del - keyword 
l=[1,2,3,4,5,6]
del (l[0])   # first item deleted 
print(l)
del l   # Deleted all item in the list 
# print(l)  # all deleted so no item there make error
l=[1,2,3,4,5,6,7,8,9,10]
del l[0: 3]
print(l)
del (l[: : 2])
print(l)

# remove - keyword - wanted value deleted from the list 
l=[1,2,3,4,5,6,7,8,9,10]
l.remove(5)   # No necessary to know the index just need the value
print(l)

#Pop - leyword -- given index value can delete / 
# Using just pop() delete the last item of the list
l=[1,2,3,4,5,6,7,8,9,10]
l.pop(l[0])
print(l)
l.pop()   # Delete the last number of the list if the index isnot given 
print(l)

# clear --- delete entire list 
l=[1,2,3,4,5,6,7,8,9,10]
l.clear()
print(l)   # Entire list deleted - blank/Empty list present 


# Operations on list 
# Arithmatic--Membership--Loop 

# Arithmatic operator (+.*)
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
print(l1+l2)  # Concatamation happen 
print (l1 * 3)  # make 3 times of the list and merge with another.


# Membership operator 
l1=[1,2,3,4,5,[6,7]]
print (5 in l1)
print (6 in l1 )    # False-- Not in the direct list but in the sublist of the list. 
print([6,7] in l1)  # True

# Loopa--
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
for i in l1:
    print (i)
for i in l2 : 
    print (i)
l=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12,]]] 
for i in l:
     print (i)


# List funtions  ---
# len/min/max/sorted
l1=[1,2,3,4,5]
print(len(l1))
print (min (l1))  # when homogenous data 
print(max(l1))
print(sorted(l1))
print(sorted(l1,reverse='True'))   # Not parmanent 

# count
l1=[1,1,2,2,3,3,3,3,4,5]
print (l.count(3)) # frequencies of the given number

#index--   Return the index of the given value 
l=[1,2,3,4,5,6]
print(l.index(3))
print(l.index(4))
#  print(l.index(9))  -- the given value isnot available so error.
#  print(l.find(9)) -- The find doesnot work in list but in string 

# N:B: If a method modifies the object itself, it often returns None.
# If a method does not modify the object, it usually returns a value or a new object.


# Reverse -- Reture the reverse of the string parmanently.
print (l[::-1])   # Not parmanently reverse jut to show 
print(l)          # So the string remain same as previous 
# l.reverse()
l=[1,2,3,4,9,2,5,6]
print(l.reverse())   # Answer is none. but changes reverse and sorted at l.
# Instead do :
l.reverse()     # used double cause we already reverse the value so need 2 time to 
                 # notice actual changes.
l.reverse() 
print(l)
print()

#Sort vs sorted  
# Sort 
l=[2,4,1,4,5,9,2,6,7]
print(l) 
print(sorted(l))   # for this moment sorted.
print(l)  # Not parmanently sorted at the previous operation.
print(l.sort()) # return none cause l.sort() return none due to parmanent opration.
print(l)   # Previous used sort make this l sorted parmanently. 
print()

# Copy  -- copied same list but in different memory address.
l=[1,2,34,6,7,7,8]
print(id(l))   # id means memory location - like pointer
l1=l.copy()    # creating new  list of the list in different memory address. (shallow memory)
print(l1)
print(id(l1))
print()

#List Comprehenion  
# List comprehension provides a concise way of creating lists.
# newlist =[expresion for item in iterable if condition == True

#Advantages of List comprehension 
# * More efficent and space-efficient than loops.
# Require fewer lines of code .
# Transforms iterative statement into a formula. 

 
# Add l to 10 numbers to a list 
l=[]
for i in range (1,11):
    l.append(i)
print(l)
# instead adding number like that use list comprehension
l=[i for i in range(1,11)]
# newlist =[expresion for item in iterable if condition == True
print(l)
print()

#scaler multiplication of a vectore 
v=[2,3,4]
s=-2
#Need out put [-4,-6,-8]
print(v*s)  # Return empty [] list 
x=[]
for i in v:
    x.append(i*s)
print(x)  #[-4, -6, -8]  # Instead use this ---> list comprehension
y=[s*i for i in v]         # Wonderful 
print(y)
print()

#Add squars
l=[1,2,3,4,5]
x=[i**2 for i in l]
print(l)
print(x)
print()

#Print all number divisible by 5 in the range of 1 to 50
l=[]
l=[i for i in range (1,51) if i%5==0]
print(l)
print()

#Find language which start with letter p  ---> mycode
languages= ['java','python','php','c','Javascript']
fl= [i for i in languages if i[0]=='p']
print(fl)
#Mentorcode
x=[language for language in languages if language.startswith('p')]
print(x)
print()

# Nested if with List Comprehension  ---> My code
basket=['apple','guava','cherry','banana']
my_fruits=['apple','kiwi','grapes','banana']
# Q. Add new list from my_fruits and item if the fruit exists in basket and also starts with 'a'
f=[i for i in my_fruits if  i in basket and i[0]=='a']
print(f)

#Mentorcode--
f=[fruit for fruit in my_fruits if fruit in basket and fruit[0]=='a']
print(f)
print()

#Print a (3*3) matrix using list comprehension --> Nested list Comprehension
f=[[i*j for i in range (1,4)] for j in range (1,4)]
print(f)
print()

#Cartesian Products -> List comprehension on 2 list together 
l1=[1,2,3,4]
l2=[6,7,8,9]
k=[(i,j) for i in l1 for j in l2]
print(k)

# 2 ways to traverse list--->
#  Itemwise 
#  Indexwise 


# Itemwise 
l=[1,3,4,5]
for i in l:
    print(i)

# Indexwise 
for  i in range (0,len(l)):
    print(l[i])

print()
#  zip() function => 
# The zip() function returns a zip object, which is an iterator of
# tuples where the first item in each passed iterator is paired together .
# and then the second item in each passed iterator are paired together.
# 
# If the passed iterator have different length , the iterator with the least items 
# decides the length of the new iterator.# 
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[-1,-2,-3,-4]
k=list[zip(l1,l2)]
print(k)
l=[(i,j) for i,j in zip(l1,l2)]
print(l)
l=[i+j for i,j in zip(l1,l3)]
print(l)


#Characteristics of list : 
# (Previous topic ) Can contain any kind of objects in python #
l=[1,2,print,type,input]    
print(l)
print()



#DIsadvantages of Python Lists
# Slow
# risky usage -- List is mutable this is the reason 
a=[1,2,3,4]
b=a
print(a)
print(b)
a.append(5)
print(a)  #[1, 2, 3, 4, 5]
print(b)  #[1, 2, 3, 4, 5]  --> but why the 5 added here cause list are mutable and poit at the same memory 
c=a.copy()
print(c)
a=a.append(7)
print(a)   #There cannot be added the 7 cause a isnot exist as list.
print(c)
#  List and print the same things.
#  eats up more memory.   