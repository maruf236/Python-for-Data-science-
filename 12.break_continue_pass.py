# Loop control Statement 

# Break 
for i in range ( 1, 10):
    if (i==5):
        break
    else :
        print(i)


# Print all prime number betweet the range 
lower = int (input ("Enter Lower range :"))
upper = int (input ("Enter Upper range :"))
for i in range ( lower , upper+1):
    for j in range (2,i):
        if (i%j==0) :# isnot prime
            break
    else:
        print(i)


# Continue 
# when loop want to skip the current itration 
for i in range ( 1,9):
    if ( i==5):
        continue
    else:
        print(i)

#Pass: when we randomly want to ignor any value 
for i in range(1,10):
    pass    