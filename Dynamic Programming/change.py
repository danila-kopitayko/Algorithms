def test(coin, amount,mem=None):
    if mem is None:
        mem = dict()

    if amount==0:
        return 0
    if amount<0:
        return -1

    if amount in mem:
        return mem[amount]

    max_int = float('inf')
    minn = max_int
    for c in coin:
        res = test(coin, amount - c,mem)

        if 0 <= res < minn:
            minn = res + 1
    mem[amount] = -1 if minn==max_int else minn
    return mem[amount]

def solution(coin, amount):
    n = len(coin)
    dp = [float('inf') for i in range(amount+1)]

    dp[0] = 0

    for i in range(1,amount+1):
        for c in coin:
            if c<=i:
                dp[i] = min(dp[i],dp[i-c]+1)

    if dp[amount] == float('inf'):
        return -1
    return dp[amount]


def main():
    print(test([1,2,5],11))
    print(solution([1,2,5],11))
    return 0

main()