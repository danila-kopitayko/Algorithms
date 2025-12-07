import random

def solution(arr):
    n = len(arr)
    dp = [1 for i in range(n)]
    for i in range(n-1):
        if arr[i+1]>arr[i]:
            dp[i+1] = dp[i] + 1
    return max(dp)

def test(arr):
    count=1
    max=0
    for i in range(len(arr) - 1):
        if arr[i+1]>arr[i]:
            count+=1
            if max<count:
                max=count
        else:
            count=1
    return max

def main():
    n = random.randint(4,10)
    arr = []

    for i in range(n):
        arr.append(random.randint(0,50))
    print(arr)
    print(solution(arr))
    print(test(arr))
    return 0

main()