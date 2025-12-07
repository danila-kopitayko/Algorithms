def solution(N):
    dp = [0 for i in range(N+1)]
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    for i in range(3,N+1):
        dp[i]=dp[i - 3] + dp[i - 2] + dp[i - 1]
    return dp


def main():
    print(solution(3))
    return 0


main()