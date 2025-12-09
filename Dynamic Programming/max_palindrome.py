def test(string):
    n=len(string)
    max_length = 0
    if n==1:
        return 1
    for i in range(1,n-1):
        for j in range(2):
            l, r = i, i+j
            while l>=0 and r<n and string[l]==string[r]:
                l-=1
                r+=1
            if max_length<r-l-1:
                max_length = r - l - 1

    return max_length

def solution(s):
    n = len(s)
    if n==1:
        return 1
    dp = [[False for i in range(n)] for i in range(n)]
    count = 0
    dp[n-1][n-1] = True
    max_length = 0


    for i in range(n-1):
        dp[i][i] = True
        if s[i]==s[i+1]:
            dp[i][i+1]=True
            if max_length<2:
                max_length = 2
    for length in range(3,n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i]==s[j] and dp[i+1][j-1]==True:
                dp[i][j]=True
                if max_length < length:
                    max_length = length
    return max_length


    


def main():
    s = 'b'
    print(test(s))
    print(solution(s))
    return 0


main()
