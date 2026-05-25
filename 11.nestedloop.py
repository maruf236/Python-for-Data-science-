#loop in loop = Nested Loop
#Q. find all pairs among 1 to 5 

# Task : 1
n=int (input("enter n: "))
for i in range ( 1, n+1):
    for j in range(0,i):
        print ('*',end="")
    print()


# Task : 2 
n = int ( input ("Enter number : "))
for i in range ( 1 , n+1, 1):
    for j in range(1, i+1 , 1):
        print (j , end="")
    for k in range (i-1, 1-1,-1):
        print (k,end="")
    print()