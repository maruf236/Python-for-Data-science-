pop=int (input('Enter current population: '))
per=float (input('Enter growth percentage: '))
import math
per=per/100
for i in range (1,101,9):
    npop=pop+pop*per
    pop=npop
    print(i,': 10 year: ',math.floor(npop))
    