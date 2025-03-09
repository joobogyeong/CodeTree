class User:
    def __init__(self, codename=" ", score=0):
        self.codename = codename
        self.score = score

user = []
for _ in range(5):
    codename, score = input().split()
    user.append(User(codename, int(score)))

min_score=user[0].score
min_user_num=0
for i in range(1,5):
    if user[i].score<min_score:
        min_score = user[i].score
        min_user_num=i

print(f"{user[min_user_num].codename} {user[min_user_num].score}")
