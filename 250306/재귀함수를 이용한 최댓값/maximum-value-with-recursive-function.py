n = int(input())
arr = list(map(int, input().split()))

def find_max(arr):
    # 원소가 하나뿐이면, 그 값이 최대값
    if len(arr) == 1:
        return arr[0]

    # 나머지 배열에서 최대값 찾기
    sub_max = find_max(arr[1:])

    # 첫 번째 원소와 비교하여 더 큰 값 반환
    return max(arr[0], sub_max)

# 테스트

print(find_max(arr))  # 출력: 10

    
    
