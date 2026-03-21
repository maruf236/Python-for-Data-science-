#Login program and indentation 
#email -> aliahsanmaruf@gmail.com
#pass -> 1234

email= input('Enter your email: ')
passw = input('Enter your password: ')
#If else syntax
#    if condition:
#          code
#    else : 
#           code


#if-else means brancing  
if email=='aliahsanmaruf@gmail.com' and  passw =='1234':
      print ('You are logged in.')
elif email=='aliahsanmaruf@gmail.com' and passw !='1234':
     print('Incorrect password.')
     passw=input('Enter password again: ')
     if passw == '1234':
          print('Welcome')
     else: 
          print('You are restricted for 30 min')
else : 
    print('Wrong email or password entered . Please try again.')

#if we have two possibilties we use if else but when have more than two
# we have to use else if -> elif in python  


#min of 3 number 
a=int(input('Enter first number :'))
b=int(input('Enter 2nd number :'))
c=int (input('Enter 3rd number :'))

if a<b and a<c:
     print('a is the smallest.',a)
elif b<a and b<c :
     print('b is the smallest.',b)
else: 
     print('c is the smallest',c)

#menu driven calculator:
a=int(input('Enter a number :'))
b=int(input('Enter 2nd number: '))
op=input('Enter the operation: ')

if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
     print(a*b)
else:
     print(a/b)