from numpy import *
j = array([])
num = int(input("Enter the number of values you want for First array:  "))
for i in range(num):
    ele = int(input("Element:  "))
    j = append(j, ele)
b = array([])
m = int(input("Enter the number of values you want for the second array:  "))
for i in range(m):
    f = int(input("Element:  "))
    b = append(b, f)
print("First Array:",j)
print("Second Array:",b)
c=j+b
print("The sum of two arrays:",c)
d = int(input("Enter the dimension of identity matrix: "))
i = identity(d, dtype="int")
print("The identity matrix of order",d,"is:")
print(i)