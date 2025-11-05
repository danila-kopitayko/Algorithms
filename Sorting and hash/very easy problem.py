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
    n1 = (max(x,y)*(n-1))//(x+y)
    time = min(x,y) + max(min(x,y)*n1,max(x,y)*(n-n1-1))
    t=0
    for i in range(max(0,n1-1),min(n-1,n1)+2):
        t = min(x,y) + max(min(x,y)*i,max(x,y)*(n-i-1))
        if t<time:
            t=time
    return t



def main():
    print(solution(1, 1, 4))
    print(solution_lcm(1, 1, 4))
    return 0

main()