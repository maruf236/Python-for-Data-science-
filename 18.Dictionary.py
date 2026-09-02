# Dictionary
# Dictionary in python is a collection of keys values , used to 
# store data values like a map, which ,unlike other dara types which hold 
# only a single value as an element . (keys -> values)
# 
# In some languages it is known as map or associattive arrays.
# 
# dict={'name': 'Ali','age': 24,'gender': 'Male'}
# 
# characteristics :
#   
# 
# Mutable 
# Indexing has no meaning .
# keys can't be duplicated 
# Keys can't be mutable items.
 


# Creating a dictionary
# Empty dictionary 
d={}
# 1D dictionary - Homogenous
d1 ={'name':'Ali', 'gender':'Male'}
# With mixed keys 
d2 ={(1,2,3): 1, 'hello':'World'}
# 2D dictionary - Hetrogenous ->JSON style
s={ 
    'name': 'Ali',
    'collage': 'Metropolitan university ',
    'Semester': 9,
     'Subjects': {
         'AI': 50, 'Web':55, 'project':53
        }
}
print(s)

#Using sequence and dict function
d4=dict([(1,1),(2,2),(3,3)])
print (d4)
d5=dict([('name','ali'),('age',24),('gender','Male')])
print (d5)
# DUplicatre keys are not allowed-- last keys update the previous value

d5={'Name':'Ahsan','age':24,'gender':'Male','Name':'Maruf'}
print (d5)

# Mutable items as keys are not allowed
# d6={'name': 'Ali', [1,2,3]: 2}   # Here list is mutable and working as keys - so not allowed
# print (d6)
d6={'name': 'Ali', (1,2,3): 2}    # Here tuple is immutable and workisng as keys - so not allowed 
print (d6)


# Accessing items from a dictionary .(dictinary is unordered so indexing not possible)
my_dict={'name':'Ali','age':24,'gender':'male'}
print (my_dict['name'])
print (my_dict['gender'])
print (my_dict.get('age')) # get method is used to access the value of a key.
print ("AI mark :" ,s['Subjects']['AI'])
s['Semester']=8
print ("Previous semester is : ",s['Semester'])

# Adding key-pair to a dictionary
print (d4)  #{1: 1, 2: 2, 3: 3}
d4['Gender']='male'
print (d4)
d4['weight']=70
print (d4)
s['Subjects']['ML']=57
print("ML mark :",s['Subjects']['ML'])
print ()
s['Subjects']['ML']=53      # Updating the value in 2D dictionary
print ("Current ML mark is : ",s['Subjects']['ML'])


# Remove key value pair from a dictionary
# pop
d1 ={'name':'Ali', 'gender':'Male',3:3,'age': 24, 'weight': 70}
d1.pop(3)
print (d1)
# popitem - Delete the last inserted key-value pair 
d1.popitem() 
print (d1)       #{'name': 'Ali', 'gender': 'Male', 'age': 24}
d1.popitem() 
print (d1)       #{'name': 'Ali', 'gender': 'Male'}
# del - total dictionary and part of dictionary can also be deleted 
del d1['gender']
print (d1)                # {'name': 'Ali'}
del d1 
# print (d1)              # The entire dictionary is deleted so printing is error 
del s['Subjects']['Web']
print (s)


# clear ---(Empty) all pairs is deleted but dictionary is present
d1= {'name': 'Ali', 'gender': 'Male'}
d1.clear()
print (d1)         # {}
print ()

# Dictionary Operations 
# Membership -- all checking is done on keys not values
# {'name': 'Ali', 'collage': 'Metropolitan university ',
#'Semester': 8, 'Subjects': {'AI': 50, 'project': 53, 'ML': 53}}
print ('ahsan' in s)        # False
print ('Subjects' in s)     # True

# Iteration 
d={'Name':'Maruf','Age': 23, 'Gender':'Male' }

for i in d : 
    print (i,":",d[i])   # print key and value


# Dictionary functions 
# length / sorted
d={'Name':'Maruf','Gender':'Male','Age': 23 }
print(len(d))
print (sorted(d))   #['Age', 'Gender', 'Name']- all keys are sorted 
                    # and returned as list
print (sorted(d,reverse=True))    # Ascending order of keys

# minimum / maximum
print (min(d))      # Base on ASCII value of keys
print (max(d))      

# Items/keys/values
d={'Name':'Maruf','Gender':'Male','Age': 23 }

print (d.items())    #dict_items([('Name', 'Maruf'), ('Gender', 'Male'), ('Age', 23)])
print (d.keys())     #dict_keys(['Name', 'Gender', 'Age'])
print (d.values ())  #dict_values(['Maruf', 'Male', 23])


# Update -- update the value of a key or add new key-value pair
d1={1:1,2:2,4:3}
d2={4:46,5:5,6:6}

d1.update(d2)   # Merge d2 into d1
print (d1)     #{1: 1, 2: 2, 4: 46, 5: 5, 6: 6}
print ()

# Dictionary comprehension
# print 1st 10 numbers and their square in dictionary .

d={i:i**2 for i in range (1,11)}
print (d)

# using exiting dictionary to create new dictionary
distances= {'Dhaka':250,'Sylhet': 300,'chittagong': 350}
miles={key :value *0.62 for (key,value ) in distances.items() }
print(miles)


# using zip
# Structure : {key:value for item in iterable }
days= ["Sunday","Monday","Tuesday","Wednessday","Thrusday","Friday","saturday"]
temp_C=[30.5,32.5,31,34,35.5,36,28]
day_tempC = {days:temp_C for (days,temp_C) in zip(days,temp_C)}
print (day_tempC)

# using if condition
# Structure : {key:value for item in iterable if condtion}
products ={'phone':10,'laptop':0,'charger':32,'tablet':0}
up_product={i:j  for i,j in products.items()  if j>0}
print (up_product)


# Nested comprehension 
tab={i:{j:i*j for j in range (1,11)} for i in range (2,5)}
print (tab)

tables={
    2:{1:2,2:4,3:4,4:8},
    3:{1:3,2:6,3:9,4:12},
    4:{1:4,2:8,3:12,4:16}
    }

