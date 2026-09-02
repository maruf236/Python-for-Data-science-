# Tuples---
# A tuple in Python is similar to a list . The difference between thw two
# is that we cannot change the elements of a tuple once if is 
# assigned whereas we can change the elements of a list.
# 
# In short , a tuple is an immutable list. A tuple cannot be changed in any way once is created.
# Characteristics--->
#                  * Ordered 
#                  * Unchangeble 
#                  * Allows duplicate . ---
# Plan of study
#      * Creating a Tuple 
#      * Accessing items 
#      * Editing items 
#      * Adding items 
#      * Deleting items 
#      * Operations on Tuples 
#      * Tuple Functions 

# Creating Tuples---
  # Empty tuple -----
t1=()
print(t1)

# Create a tuple with a single item 
t2=(2)
print(t2)         # t2 become a integer datatype not a tuple.
print(type(t2))   #<class 'int'>
t2=('hello')
print(type(t2))   #<class 'str'>
t2=('hello',)     # --- Single item tuple 
print(type(t2))   #<class 'tuple'>
print(t2)         #('hello',) -- same as list just has 1st bracket 
#Homogenous tuple 
t3=(1,2,3,4)
print(t3)
#Hetrogenous tuple 
t4=(1,2,3,4,True,[1,2])
print(t4)
#Using type conversion 
t5=tuple('hello')
print(t5)         #('h', 'e', 'l', 'l', 'o')

#Accessing items from a tuple---
#Indexing -----  Slicing 
t3=(1,2,3,4)
print(t3[0])      # 1
print(t3[-1])     # 4
print()
print(t3[0:4:2])     #(1, 3)
print(t3[ ::-1])     #(4, 3, 2, 1)
t4=(1,2,3,(4,5))     
print(t4[-1][0])     #4
print()
t3=(1,2,3,4)
print(t3[-3:])        # (2, 3, 4)
print(t3[-1:-4:-1])   #(4, 3, 2)
#Editing items ----- Tuple is immutable so not possible to change/Edit
# t3[0]=100    --- TypeError: 'tuple' object does not support item assignment.

#Adding item ---same not possible to change -- editing 

#Deleting items --- full tuple can be deleted but a portion cannot be ->  same word immutable.
print(t3)
del(t3)
# print(t3)  --- error cause the t3 in not defiend/deleted. 
# del(t4[-1][0]) --- Doesnot work . 
print()

#Operation on Tuples
# + and  *
t1=(1,2,3,4,9)
t2=(5,6,7,8)
print(t1+t2)   #Merge--(1,2,3,4,9,5,6,7,8)
print(t1*3)    #t1 is 3 times and merge --(1, 2, 3, 4, 9, 1, 2, 3, 4, 9, 1, 2, 3, 4, 9)

# Membership 
print(1 in t1 )    # 1 present in t1 -- True
print(5 in t2 )    # 5 present in t2 -- True
print(9 in t2 )    # 9 present in t2 -- False
print(9 not in t2) #True

#iteration 
for i in t1 :
    print(i,end=' ')   # using loop printing 
print()

# Tuples function --- 
#len/sum/min/max/sorted ---
t1=(1,2,3,4,5,6)
print(len(t1))
print(sum(t1))  # sum of all number 
print(min(t1))
print(max(t1))
print(sorted(t1))  # as list
print(sorted(t1,reverse=True))


#Count 
t1=(1,2,3,4,5,6)
print(t1.count(23))
print(t1.count(1))
print(t1.count(4))

#index 
print(t1.index(3))   # 0 indexing 
print(t1.index(6))   # 0 indexing 

# Difference between Tuples  and  Lists 
#       *Syntax   -- small and square bracket 
#       *Mutability -- list is mutable but not tuple.
#       *Speed -- tuples are faster than list (Immutable are always faster than mutable.)


#import time   # Use all time counting related things
#L=list(range(100000))
#T=tuple(range(100000))
#start = time .time ()
#for i in L:
#    i*5
#print('List time ',time.time()-start)

#start= time.time()
#for i in T:
#    i*5
#print('Tuple time',time.time()-start)



#       *Memory ---  tuples hold less than List(Immutable datatype take more place than mutable ) 
import sys
L=list(range(1000))
T=tuple(range(1000))

print('list size',sys.getsizeof(L)) # getsizeof can detect how much memrory consume
print('Tuple size',sys.getsizeof(T))

#       *Built in functionality
#       *Error prone -- List is more error prone . Tuple are good.
a=[1,2,3,4]
b=a
a.append(5)
print(a)
print(b)
#Whereas --- // cannot use a.append in tuple  . 
a=(1,2,3,4)
b=a
a=a+(5,)
print(a)
print(b)
#       *Usability --- tuple for fixed use like result sheet but List is changeble as we want .

#Tuple unpacking 
a,b,c=(1,2,3)
print(a,b,c)
# a,b=(1,2,3)  -- too many values to unpack (expected 2, got 3)

# Swaping -- Different way.
a=1
b=2
a,b=b,a
print(a,b)

# need first two value not other-- Tuple unpacking 
a,b,*others=(3,4,5,1,2)
print(a,b)

# Zipping tuples 
a=(1,2,3,4)
b=(7,5,9,6)
print(zip(a,b))   #--- Become a zip object
print(list(zip(a,b)))  #--- zip converted to a tuple--2D

#Summery --- Every read operation are allowed to tuple but not the write operation 
# due to immutability.




