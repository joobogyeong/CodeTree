
n = int(input())

move_cost = list(map(int, input().split()))   # 장소 사이 이동에 필요한 에너지
charge_cost = list(map(int, input().split())) # 각 장소에서 에너지 1을 채우는 비용

answer = 0
min_cost = charge_cost[0]

for i in range(n - 1):
    min_cost = min(min_cost, charge_cost[i])
    answer += min_cost * move_cost[i]


print(answer)