class Human:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h  
        self.w = w

human = []
for i in range(5):
    name, h, w = tuple(input().split())
    human.append(Human(name, int(h), w))

human.sort(key = lambda x : x.name)
print('name')
for hu in human:
    print(hu.name, hu.h, hu.w)
human.sort(key = lambda x : -x.h)
print()
print('height')
for hu in human:
    print(hu.name, hu.h, hu.w)