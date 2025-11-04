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
    return l + min(x,y)

def solution_lcm(x,y,n):
    lcm = math.lcm(x,y)
    amount = math.floor(n*x*y//(lcm*(x + y)))
    print(f'lcm={lcm}')
    #time = lcm*amount
    time_big = 0
    time_small = 0
    if amount*(lcm/x + lcm/y)>=n-1:
        count=0
    else:
        count = amount*(lcm/x + lcm/y)
    rest = (n - count - 1)*min(x,y)
    time = 0
    print(f'beginning:\ntime={time}\ncount={count}\nrest={rest}')
    additional_time = 0
    if count<n-1 and rest//max(x,y)==0:
        count+=n-count - 1
        time+=rest
        print(f'rest//max(x,y)==0:\ntime={time}\ncount={count}')
        return time
    elif rest//max(x,y)!=0:
        time+=(rest//max(x,y)) * max(x,y)
        time_big+=1
        count+=(rest//max(x,y))
        print(f'rest//max(x,y)!=0:\ntime={time}\ncount={count}')
    while count<n:
        #time+=min(x,y)
        time_small+=1
        count+=1
        if time_small*min(x,y)>time_big*max(x,y):
            time+=time_small*min(x,y)-time_big*max(x,y)
    return time


    count+=1
    #print(time)
    #return time+min(x,y)


    #print(time)
    return time+min(x,y)



def main():
    iter = random.randint(5,15)
    print(solution(2, 3, 5))
    print(solution_lcm(2, 3, 5))
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