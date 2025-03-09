class User:
    def __init__(self, codedname=" ", score):
        self.codename = codename
        self.score = score

user =[
    tuple(map(input().split()))
    for _ in range(5)
]
min=user[0].score
name=""
for i in range(1, 5):
    if user[i].score<min:
        min=user[i].score
        name=user[i].codename
print(f"{name} {min}")
