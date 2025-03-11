n=int(input())
class Human:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h  
        self.w = w

human = []
for i in range(n):
    name, h, w = tuple(input().split())
    human.append(Human(name, int(h), w))

human.sort(key = lambda x : (-x.h, -x.w))
for hu in human:
    print(hu.name, hu.h, hu.w)
