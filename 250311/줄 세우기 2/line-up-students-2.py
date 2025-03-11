n=int(input())
class Student:
    def __init__(self, h, w, num):
        self.h=h
        self.w=w
        self.num = num
student=[]
for i in range(1, n+1):
    h, w = list(map(int, input().split()))
    student.append(Student(h,w,i))

student.sort(key = lambda x:(x.h, -x.w))

for s in student:
    print(s.h, s.w, s.num)
