def solution(s,k):
    right_balance = 0
    balance = 0

    for i in range(len(s)):
        if s[i]=='(':
            balance+=1
        else:
            if balance>0:
                balance-=1
            else:
                right_balance+=1
    total = right_balance + balance
    return total <= k



def main():
    s = ')()'
    print(test(s,1))
    print(solution(s,1))
    return 0


main()