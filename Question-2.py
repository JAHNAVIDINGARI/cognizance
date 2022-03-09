from numpy import*
j = array([])
num = int(input("Enter the number of elements  you want for First array:  "))
for i in range(num):
    e = int(input("Element:  "))
    j = append(j, e)
b = array([])
m = int(input("Enter the number of elements  you want for the second array:  "))
for i in range(m):
    f = int(input("Element:  "))
    b = append(b, f)
print("First Array:",j)
print("Second Array:",b)
c=j==b
e=c.all()
print(e)
