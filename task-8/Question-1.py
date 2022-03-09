from numpy import *
j=array([])
first=int(input('First Number:'))
last=int(input('Last Number:'))
for i in range(first,last):
    j=append(j,i)
    for i in range(5):
        j=append(j,0)
j=append(j,last)
print(j)