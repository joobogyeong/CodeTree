n=int(input())

class Person:
    def __init__(self, name='', korean=0, english=0, math=0):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

people=[]
for _ in range(n):
    name, korean, english, math = tuple(input().split())
    people.append(Person(name, korean, english, math))

people.sort(key=lambda x:(-x.korean, -x.english, -x.math))

for i in range(n):
    print(f"{people[i].name} {people[i].korean} {people[i].english} {people[i].math}")
