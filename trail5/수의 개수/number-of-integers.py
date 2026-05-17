N, M = map(int, input().split())
arr = list(map(int, input().split()))

def upper_bound(target):
    global N
    left = 0
    right = N-1
    min_idx = N

    while (left <= right):
        mid = (left + right) // 2
        if arr[mid] > target:
            min_idx = min(min_idx, mid)
            right = mid -1
        else:
            left = mid + 1
    return min_idx
    
def lower_bound(target):
    left = 0                             
    right = N - 1                        
    min_idx = N

    while (left <= right): 
        mid = (left + right) // 2        
        if arr[mid] >= target:           
            min_idx = min(min_idx, mid)  
            right = mid - 1              
        else:
            left = mid + 1               
    
    return min_idx                       

for _ in range(M):
    num = int(input())
    upper_idx = upper_bound(num)
    lower_idx = lower_bound(num)
    print(upper_idx - lower_idx)

