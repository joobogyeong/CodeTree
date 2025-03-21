N = int(input())  # 숫자의 개수 입력
array = [int(input()) for _ in range(N)]  # N개의 숫자 입력받기

cnt = 0
max_cnt = 0

for i in range(N):
    if i == 0 or array[i] == array[i - 1]:  # 첫 번째 원소거나, 이전 원소와 같다면 카운트 증가
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)  # 최대 연속 길이 업데이트
        cnt = 1  # 새로운 숫자가 나오면 다시 1부터 시작

max_cnt = max(max_cnt, cnt)  # 마지막 남은 cnt 반영

print(max_cnt)  # 최대 연속 길이 출력
