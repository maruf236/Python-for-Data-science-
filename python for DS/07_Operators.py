#arithmetic Operator
print (4+3)
print(42-23)
print (23*2)
print (234/7)
print(5//2) #Integer division-> The quetient turn into integer
print( 5%2)
print(5**2 ) #% to the power 2 (5*5=25)

#Relational Operator
print(4>5)
print (4<5)
print(4>=4)
print(4<=4)
print(4==4)
print(4!=4)

#Logical operator
print (1 and 0)
print (1 or 0)
print (not 1)

#Bitwise operators
print(5 & 4) # bitwise and 5->101 4->100 afer AND 010
print(5|4)   #5->101  4->100 after OR 101
print(5^4)   #5->101  4->100 after XOR 001  same is 0 diff is 1
print(~5)
print(4>>2)
print (5<<2)


#Assingment Operators
#  ' = '
a=2
a+=2 #a=a+2
a-=2 #a=a-2
#like c and c++  a++ and a-- isnot allowed


#Membership Operator
#in/not in 

print('a' in 'Dhaka')
print('A' not in 'Dhaka')
print (1 in [2,3,4,55,6,7,4])

#Program - Find the sum of a 3 digit number entered by the user
a=input('Enter 3 digit number : ')
a= int (a)
b=a%10
sum=0
sum+=b
a=int(a/10)
b=a%10
sum+=b
a=int(a/10)
sum+=a
print(sum)
