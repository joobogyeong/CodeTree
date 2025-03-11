n=int(input())
class Student:
    def __init__(self, name='', sub1=0, sub2=0, sub3=0):
        self.name = name
        self.sub1 = int(sub1)
        self.sub2 = int(sub2)
        self.sub3 = int(sub3)

student = []
for i in range(n):
    name, sub1, sub2, sub3 = tuple(input().split())
    student.append(Student(name, sub1, sub2, sub3))

student.sort(key = lambda x:x.sub1+x.sub2+x.sub3)
for i in range(n):
    print(f"{student[i].name} {student[i].sub1} {student[i].sub2} {student[i].sub3}")
