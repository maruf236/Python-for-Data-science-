## Operation on string 
#   *Aroithmatic Operation 
#   *Relational Operation 
#   *Logical Operation 
#   *Loops On Strings 
#   *Membership operation 


# Arithmatic Operation ( only + and * )
print ('Dhaka ' + 'Sylhet ') # Concatanation happen 
print ("Dhaka " * 5)   # 5 times dhaka printing

# Realational Operation 
print ("dhaka"== "Sylhet ") # False  
print ("Sylhet"=="Sylhet") # True 
print ("Dhaka" > "Sylhet") # false = string comapare with lexicographically 
print ("Dhaka" < "Sylhet") # True ' Think like Dictionary '


# Logical operation
# Empty string means False . 
# Not empty string/ Has character in the string is True .
print ('Hello ' and 'world') # World 
print ('hello ' or  'World') # Hello

# OR= when compiler get the true value i the operation it doesnot 
# required to check the next string to get the result . so it 
# immediatly  print the string .   But if get 1st false then will try to check the 2nd one 
# to get the result true or flase. 
# 
# AND= when compiler get the reuslt true it will must check the 
# 2nd string to decide the final answer. cause AND operation answer could change on 
# the 2nd condition.

print(not '') # True
print (not 'Hello') # False 


#LOOPs On string 

for i in  ('hello world'): # Range use for integer 
    print(i) # In loops True means execute false means break

for i in  ("Dhaka"): # Range use for integer not for string 
    print ('sylhet')



# Common  string Function ( applicable for any datatype)
# len - max - min - sorted 
s= 'hello world'
# len - the length of the string including space 
print ( len(s)) # 11
# max - The maximum value (ASCII)  character in the string 
print (max (s)) # w
# min - the minimum value ( ASCII) character in the string 
print ( min (s))
# Sorted - The ascending order sorting 
# The sorted string result is  list() in ascending order
print ( sorted(s))
# Reverse sorting - sorted(s,reverse= True )
print ( sorted(s,reverse=True))


#Capitalize/ Title / Upper / Lower / Swapcase

# s.capitalize()- make the first letter Capital and doesnot save
#               it automaticaly , so need to save it during this operation 
#             the string is immutable we do capital and save as new string . 
#              for save the capitalize string we need to save the string again.
s= 'hello world' 
s= s.capitalize()  #
print(s)

# s.title() - make every first letter  of the word capital in this string 
s= "I love my country - Bangladesh"
s= s.title()
print (s) # I Love My Country - Bangladesh

#s.upper() - make the entire character in the string capital. 
s=s.upper()  #I LOVE MY COUNTRY - BANGLADESH
print (s)

#s.lower() -make the entire letter in the string smaller .
s=s.lower()  #i love my country - bangladesh
print (s)

#s.swapcase() - make the lowercase the upper and the viceversa.
s='i loVe YoU'
s=s.swapcase()
print (s)     #I LOvE yOu


# Count  / Count  / Index

#count('c') - make count the substring/character frequencies in the given string 
s = ' my name is Ahsan'
a=s.count('a')
print(a)             # 2
print(s.count('n'))  # 2

# Find('c') - find the substring/character index in the given string 
s='My name is ali ahsan maruf'
print( s.find('ali'))       # 11
print( s.find( 'ahs'))      # 15
print( s.find('x'))       # -1 = if answer isnot there then result is -1

#index() - same as find . diff is - If the index doesnot exist then make error not like find showing -1 
print( s.index('ah'))
# print( s.index('x'))

#Endswith / startswith

#endswith('c') - Does given string ended with this particular word ( True/ false)
print( s.endswith('uf'))   # True 
print( s.endswith('an'))   # False

#startswith()- Does given string starts with this particular string or not ( True / False )
print ( s. startswith('My'))     # True
print ( s.startswith('ali'))     # False

# format() - it can pass the some stored string value to the blank string place.
# Order matters - first is to first / 2nd is to 2nd 
name = 'Maruf'
gender = 'male'
sent= 'Hi my name is {} and I  am a {}.'
print( sent.format(name, gender ))     #Hi my name is Maruf and I  am a male.
print( sent.format(gender, name ))     # order not maitained 
sent= 'Hi my name is {1} and I  am a {0}.'  
print( sent.format(gender, name ))     # Order maintained - using serial 0,1


#isalnum() / isalpha()  / isdigit() / isidentifier()

#isalnum()- is the string alphabet and numeric (alphanumeric? True and false 
s='aliahsanmaruf115'
print ( s.isalnum())      # True - Alphabet and Number  ( also could't contain space )
s='Ali ahsan maruf 115%'
print ( s.isalnum())     # False - have extra character excluded Alphabet and Number 

#isalpha()- is the string contain only alphabet or not (true or false )
s="AliAhsanMaruf"
print( s.isalpha())   # True 
s="ALi Ahsan Maruf 115"
print( s.isalpha())      # False - Have space and digit

#isdigit()-  is the string is containing only number or not (True or false )
s='123567'
print(s.isdigit())     # True 
s='1111111234s'
print(s.isdigit())    # False- have character 

#isidentifier()- depending on the indentifier rules is it possible or not ( True or false )
i= '123abcd'
v= "String_operation"
print( i.isidentifier())      # False - has number in the beginning
print( v.isidentifier())      # True - no issue. used underscore not space 


# Split / join / replace /  strip

#split - make split in every word (at space) or given letter in the split ('i') 
#         but the selected letter is use to split not present in the answer . 
# most usable
m= ' my name is maruf '
print(m.split())          #['my', 'name', 'is', 'maruf']
print(m.split('i'))       #[' my name ', 's maruf ']
print(m.split('is'))      #[' my name ', ' maruf ']


#" ".join(s)  -  just attach space between two word or attach the given character between two word before join instruction. 
s=['my', 'name', 'is', 'maruf']
print(" ".join(s))    # my name is maruf
print("-".join(s))    # my-name-is-maruf


#replace() - replace particular substring in the given string 
s= 'My name is Maruf'
print (s.replace('Maruf','Ali Ahsan Maruf'))    #My name is Ali Ahsan Maruf
#-> find the 'Maruf' then replace with 'Ali Ahsan Maruf'
#We cannot change or do surgery on the original operation . we make new string to show it . 
print(s.replace('Maruf12', 'Maruf115'))      # My name is Maruf

#Strip
s='ali ahsan maruf            '
print(s.strip())