class User:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

users = []  # 사용자 객체를 저장할 리스트

# 5명의 데이터를 입력받아 User 객체 생성
for _ in range(5):
    codename, score = input().split()
    users.append(User(codename, int(score)))

# 점수가 가장 낮은 사용자 찾기
min_user = min(users, key=lambda user: user.score)

# 결과 출력
print(f"{min_user.codename} {min_user.score}")
