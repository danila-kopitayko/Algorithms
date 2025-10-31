import random
import numpy as np

def find_sqrt(target):
    l = 0
    r = target
    while l<=r:
        middle = (l+r)//2
        #print(f'middle={middle}')
        if middle**2>target:
            r = middle - 1
            continue
        elif middle**2<target:
            l = middle + 1
            continue
        return middle

def test(target):
    return int(np.sqrt(target))

def main():
    n = random.randint(10,100)
    for i in range(n):
        t = random.randint(1,10)
        if test(t**2)!=find_sqrt(t**2):
            print(f"ALARM\ntest={test(t)}\tsol={find_sqrt(t)}")
            return -1
        else:
            print('OK')
    #print(f'target={t**2}')
    print(find_sqrt(t**2))
    return 0

main()


