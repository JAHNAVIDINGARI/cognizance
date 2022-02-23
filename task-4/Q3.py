num = int(input("Enter The Number of Students : "))
temp = [['Roll No','Name','Marks']]
for p in range(num):
    roll_no = input('Enter Roll No : ')
    student_name = input('Enter Student Name : ')
    marks = int(input('Enter Marks : '))
    temp.append([roll_no,student_name,marks])
for p in range(len(temp)):
    for q in range(len(temp[p])):
        k=temp[p][q]
        print(k,end='\t')
    print('\n')
c=int(input('Enter The Row to be Printed : '))
for p in temp[c]:
    print(p,end='\t')
