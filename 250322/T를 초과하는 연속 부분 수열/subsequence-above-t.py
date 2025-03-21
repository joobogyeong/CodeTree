N, T = map(int, input().split())
array = list(map(int, input().split()))

cnt = 0
max_cnt = 0

for i in range(N):
    if array[i] > T and (i == 0 or array[i] > array[i - 1]):  # 첫 번째 요소이거나 증가하는 경우
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)  # 최대 연속 길이 업데이트
        cnt = 0  # 연속이 끊어지면 0으로 초기화

max_cnt = max(max_cnt, cnt)  # 마지막 연속된 값 고려

print(max_cnt)
