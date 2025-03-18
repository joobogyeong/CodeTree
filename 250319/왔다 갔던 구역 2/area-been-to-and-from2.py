N = int(input())  # 명령 개수 입력
arr = [tuple(input().split()) for _ in range(N)]  # (거리, 방향) 입력

result_array = [0] * 1000  # 충분히 큰 배열 (좌우 이동 고려)
current_point = 500  # 초기 위치를 500으로 설정

for i in range(N):
    distance = int(arr[i][0])  # 거리 (정수 변환)
    direction = arr[i][1]  # 방향 ('R' 또는 'L')

    if direction == 'R':  # 오른쪽으로 이동
        for _ in range(distance):
            result_array[current_point] += 1
            current_point += 1
    else:  # 왼쪽으로 이동
        for _ in range(distance):
            result_array[current_point] += 1
            current_point -= 1  # 왼쪽으로 이동이므로 감소

# 2번 이상 지나간 위치 개수 세기
cnt = sum(1 for elem in result_array if elem >= 2)

print(cnt)
