N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: x[1])
cnt = 0
end_point = 0
for time in meetings:
    if time[0]>=end_point:
        cnt+=1
        end_point = time[1]
print(cnt)

    
