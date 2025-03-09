class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color =color
        self.second = second

code, color, second = input().split()
delet_bomb = Bomb(code, color, int(second))
print(f"code : {delet_bomb.code}")
print(f"color : {delet_bomb.color}")
print(f"second : {delet_bomb.second}")

