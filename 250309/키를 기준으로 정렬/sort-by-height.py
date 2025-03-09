n=int(input())

class Person:
    def __init__(self, name="", hight=0, weight=0):
        self.name = name
        self.hight = hight
        self.weight = weight

people=[]
for _ in range(n):
    name, hight, weight = tuple(input().split())
    people.append(Person(name, hight, weight))

people.sort(key=lambda x:x.hight)

for i in range(n):
    print(f"{people[i].name} {people[i].hight} {people[i].weight}")
