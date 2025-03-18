N=int(input())
arr=[
    tuple(input().split())
    for _ in range(N)
]
result_array=[0]*2000
current_point=1000
for i in range(N):
    if arr[i][1]=='R':
        for _ in range(int(arr[i][0])):
            result_array[current_point]+=1
            current_point+=1
    else:
        for _ in range(int(arr[i][0])):
            result_array[current_point]+=1
            current_point-=1
total_length = 0
in_segment = False
segment_length = 0  # 현재 구간의 길이

for i in range(len(result_array)):
    if result_array[i] >= 2:
        if not in_segment:  # 새로운 구간이 시작됨
            in_segment = True
            segment_length = 1  # 현재 위치 포함
        else:
            segment_length += 1  # 연속된 부분이므로 길이 증가
    else:
        if in_segment:  # 구간이 끝났다면 길이 합산
            total_length += segment_length
            in_segment = False
            segment_length = 0  # 초기화

# 마지막 구간이 종료되지 않았을 경우 처리
if in_segment:
    total_length += segment_length

print(total_length)