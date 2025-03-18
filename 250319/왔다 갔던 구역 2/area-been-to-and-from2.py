N = int(input())
arr = [tuple(input().split()) for _ in range(N)]

result_array = [0] * 2000  # 충분한 크기의 배열 확보
current_point = 1000  # 중앙에서 시작

for distance, direction in arr:
    distance = int(distance)  # 정수 변환

    if direction == 'R':  # 오른쪽 이동
        for _ in range(distance):
            current_point += 1  # 먼저 이동
            result_array[current_point] += 1  # 방문 횟수 증가
    else:  # 왼쪽 이동
        for _ in range(distance):
            current_point -= 1  # 먼저 이동
            result_array[current_point] += 1  # 방문 횟수 증가

# 2번 이상 방문한 영역 개수 세기
cnt = sum(1 for visits in result_array if visits >= 2)
print(cnt)
