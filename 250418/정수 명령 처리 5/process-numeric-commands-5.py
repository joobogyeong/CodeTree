import sys
input = sys.stdin.readline

n = int(input())  # 명령어 수
arr = []

for _ in range(n):
    cmd = input().strip()
    
    if cmd.startswith("push_back"):
        _, val = cmd.split()
        arr.append(int(val))
        
    elif cmd == "pop_back":
        if arr:
            arr.pop()
    
    elif cmd == "size":
        print(len(arr))
        
    elif cmd.startswith("get"):
        _, idx = cmd.split()
        print(arr[int(idx)])
