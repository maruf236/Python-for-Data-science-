# Loops : doing same thing repeatedly till the condition make false
# 3 types : for loop, while loop, do-while
# Uses :     

# While loop

num1 =int(input("Enter a number : "))

i=1
while i<11:
    print(num1 ,'*', i,'=', num1*i )
    i+=1   # Use python tutor to visualize the code 



# while loop with else
x=1
while x<3: 
    print(x)
    x+=1
else: print("Limit Exceded")

#Guessing game

# Generate Random integer between 1 to 100

import random
jackpot = random.randint(1,100)
guess= int (input("Guess a number : "))

i=1
while (jackpot!=guess) :
    if(guess<jackpot):
        print("Think above the number ")
    else:
        print("Think lower the number ")
    guess=int(input())
    i+=1
else: 
    print("You guess the correct number at ",i,"th tries")


#For loop: Powerful and easy 
#For loop use range

for i in range (1,10,2):  # it means 1 to less than 10 
   #(starting, less than ending, differences)
    print(i)
for i in range (10,0,-1):
    print (i)

for i in 'Bangladesh':
    print (i)    

for i in [1,2,3,4,5,6,9]:
    print(i)
for i in {1,2,3,4,5,6,7}:
    print(i)    