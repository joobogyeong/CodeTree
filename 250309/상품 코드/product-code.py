class User:
    def __init__(self, id, level):
        self.id=id
        self.level=level

user1 = User("codetree", 50)
user_name, user_level = input().split()
user2 = User(user_name, user_level)
print(f"product {user1.level} is {user1.id}")
print(f"product {user2.level} is {user2.id}")