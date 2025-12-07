def recursive(row,col):
    if col==0 or col==row:
        return 1
    else:
        return recursive(row-1,col-1) + recursive(row-1,col)

def test(n):
    arr = []
    for row in range(n):
        current_row = []
        for col in range(row + 1):
            current_row.append(recursive(row,col))
        arr.append(current_row)

    return arr


def solution(n):
    dp = []
    for i in range(1,n+1):
        dp.append([1 for k in range(i)])
    for i in range(2,n):
        for j in range(1,i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    return dp


def main():
    print(test(5))
    print(solution(5))
    return 0

main()