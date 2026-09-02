# Sets
#  A set is an unordered collection of items . Every set element is unique (no duplicate) 
# and must be immutable (cannot be changed). 
# However , a set itself is mutable .  We can add or remove items from it . 
# Sets can also used to perform mathematical ste operations like union ,
# intersection ,symmetric difference,etc.
# 
# Characteristics:
#        @ unordered 
#        @ Mutable 
#        @ No duplicate 
#        @ Can't  contain mutable data types.

print()
print()

# Creating sets
#Empty sets 
s={}
print(s)
print (type(s))   # Type is dictionary .... so careful
# create an empty set - correct way 
s=set()
print(type(s))    # Type is set
s1={1,2,3,4,5}    # 1D set -- homogenous set 
print(s1)
# s1={1,2,3,{23,45}}   # Not allowed mutable data type inside of a set.
print(s1)
# Hetrogenous set
s3={1,'hello',4.5,True}
print(s3)        # {1, 4.5, 'hello'} -- cannot have Duplicate #Unordered 
s2={1,2,4,5,(6,7,8),'hello'} 
print(s2)
# using type conversion 
s4=set([1,2,4,5,6])  # Lsit to set 
print(s4)
s5={1,2,3,3,4,4,5,5}
print(s5)            # {1, 2, 3, 4, 5}  Duplicate arenot allowed
# Set cannot have mutable data type 
# s={1,2,3,4,[5,6,7]}
# print(s)

s1={1,2,3}
s2={3,1,2}
print(s1==s2)   # True - if content same 

# Accessing item 
s1={1,2,3,4,5}   # unordered so indexing impossible
# print (s[1])   no positive or negative or slicing not possible 

# Editing
s1={1,2,3,5}
# s1[1]=100   # In set indexing not works so editing also no work.
print(s1)

# Adding items 
s1={1,2,3,5}
#s1.add(6)    # Single item adding-6  -- Place decide by hashing 
print(s1)
s1.update([5,6,7])  # Have to pass usong list style 
print(s1)

# Deleting items
# del
s1={1,2,3}
print(s1)
del s1
# print(s1) Deleted

# cannnot delete the indexed value cause index not working in set .

# discard --- sending the value to delete.
s1={1,2,3}
s1.discard(3)
print(s1)        #{1, 2} -- 3 deleted 
s1.discard(20)
print(s1)     # Even the 20 isnot present in set it doesnot show any error . 

#remove -- works as discard 
s1={1,2,3,4,5}
s1.remove(5)
print(s1)     # but 
# s1.remove (20)   - The main difference between the discard and the remove is 
#  print (s1)      - remove show error during removing uninserted value but the discard doesnot .

#  pop --- randomly delete any item . 
s1={1,2,3,4,5}
s1.pop()
print (s1)      # Randomly - 1 deleted {2, 3, 4, 5}


# Clear --- make the set empty 
s1.clear()
print (s1)      # Empty - set()

# Operations of sets
#Union -- combine two sets
s1={1,2,3,4}
s2={3,4,5,6}
print (s1|s2)
#Intersection -- common items
print(s1 & s2)
#Difference -- items in s1 but not in s2
print(s1-s2)
#Symmetric difference -- items in s1 or s2 but not both
print(s1^s2)
#Membership -- check if an item is in a set -True / false
print (2 in s1)
print (9 in s2)
print (1 not in s2 )
for i in s1:
    print (i,end =' ')
print ()

#set funtions
#length/sum/min/max/sprted 
s1={1,2,3,4,5}
print (len(s1))
print (sum(s1))
print (min (s1))
print (max (s1))
print (sorted (s1))      # Result as list [1, 2, 3, 4, 5]
print (sorted (s1,reverse=True)) #[5, 4, 3, 2, 1]

#Union /update 
s1={1,2,3,4}
s2={3,4,5,6}
s1.union(s2)     # print (s1|s2)
s1.update (s2)   #Union operation on s1 and s2 and save to s1 / s2 untouched 
print (s1)       #{1, 2, 3, 4, 5, 6}
print (s2)
print()

#Intersection / intersection_update 
s1={1,2,3,4}
s2={3,4,5,6}
print(s1.intersection(s2))  # print (s1 & s2)
s1.intersection_update(s2) # Intersection operation on s1 and s2 and save to s1 / s2 untouched
print (s1)               #{3, 4}
print (s2)               #{3, 4, 5, 6}


#Difference / differcnce_update 
s1={1,2,3,4}
s2={3,4,5,6}
print (s1.difference(s2))          #{1, 2}
s1.difference_update (s2)     # Difference operation on s1 and s2 and save to s1 / s2 untouched
print (s1)                #{1, 2}
print (s2)                #{3, 4, 5, 6}

print ()

#symmetric difference / symmnetric_difference_update  
s1={1,2,3,4}
s2={3,4,5,6}
print(s1.symmetric_difference(s2))    #{1, 2, 5, 6}
s1.symmetric_difference_update(s2) 
print (s1)                           #{1, 2, 5, 6}
print (s2)                           #{3, 4, 5, 6}


#isdisjoint/issubset/issuperset 
s2={3,4,5,6}
print ()
print(s1.isdisjoint(s2))  # Returns True if the sets have no common elements
print (s1.issubset(s2))   # Returns True if all elements of s1 are in s2
print (s1.issuperset(s2)) # Returns True if all elements of s2 are in s1

#Copy
s1={1,2,3,4}
s2=s1.copy()
print (s1)
print (s2)
print ()


# Frozen set = is just an immutable version of a python set object
fs=frozenset([1,2,3,4])
print (fs)           # Immutable set- cannot change the elements .
fs1=frozenset([1,2,3,4])
fs2=frozenset([3,4,5,6])
print (fs1 | fs2)     # Every result of set operation is also a frozen set.
print (fs1 ^ fs2)
print (fs1 & fs2)
# Works -> all read operation
# doesnot works -> all write operation

#2D frozen set 
fs1 =frozenset([(1,2,3),(4,5,6)])
fs2= frozenset([(4,5,5),frozenset([1,2,3])])


# Set comprehension 
sc={i for i in range(4,10)}
print(sc)
print()
print ()
