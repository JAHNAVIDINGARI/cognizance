a=int(input("Enter number:"))
check=a
rev=0
while(a>0):
    num=a%10
    rev=rev*10+num
    a=a//10
if(check==rev):
    print('True')
else:
    print('False')
