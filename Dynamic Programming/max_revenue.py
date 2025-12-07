def solution(arr):
    n = len(arr)
    dp = [0 for i in range(n)]
    ptr = arr[0]
    maxx = 0
    for i in range(1,n):
        if arr[i]>ptr:
            dp[i] = arr[i] - ptr
            if maxx<dp[i]:
                maxx=dp[i]
                print('maxx=',maxx)
        else:
            ptr = arr[i]
            print('ptr=',ptr)
    return dp



def main():
    arr = [7,6,5,4,3,2,1]
    print(solution(arr))
    return 0

main()