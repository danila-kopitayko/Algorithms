import random
import math

def solution(x,y,n):
    l = 0
    r = (n - 1) * max(x,y)
    while l+1<r:
        m = (l + r) // 2
        if m // x + m // y <= n-1: #количество копий, которые ксерокрсы вместе смогу сделать за время m
            l = m
        else:
            r = m
    return r + min(x,y)

def solution_lcm(x,y,n):
    lcm = math.lcm(x,y)
    amount = math.floor(n*x*y//(lcm*(x + y)))
    time = lcm*amount
    count = 0
    print('asdfasdf',amount)
    while amount<n:
        print(f'amount={amount},time={time}')
        amount+=1
        time+=min(x,y)
    return time+min(x,y)


    #print(time)
    return time+min(x,y)



def main():
    iter = random.randint(5,15)
    print(solution(5, 3, 9))
    print(solution_lcm(5, 3, 9))
    '''    for i in range(iter):
        n = random.randint(0, 10)
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        if solution(x,y,n)!=solution_lcm(x,y,n):
            print('ALARM')
            print(f'iteration={i}\tx={x} y={y} n={n}\nsol={solution(x, y, n)}\tlcm={solution_lcm(x, y, n)}')
            return -1'''
    return 0

main()