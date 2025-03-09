class User:
    def __init__(self, id, level):
        self.id=id
        self.level=level

user1 = User("codetree", 10)
user_name, user_level = input().split()
user2 = User(user_name, user_level)
print(f"user {user1.id} lv {user1.level}")
print(f"user {user2.id} lv {user2.level}")