def solution(N):
    dp = [0 for i in range(N+1)]
    dp[0] = 1
    dp[1] = 2
    #print(dp)
    for i in range(2,N+1):
        #print(i)
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]

def main():
    print(solution(3))
    return 0

main()