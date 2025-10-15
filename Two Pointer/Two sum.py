import random
def solution(arr,target):
    n = len(arr)
    p1, p2 = 0, n-1
    while p1<p2:
        print(arr[p1],arr[p2],target)
        if arr[p1] + arr[p2] < target:
            p1+=1
        elif arr[p1] + arr[p2] > target:
            p2-=1
        elif arr[p1] + arr[p2] == target:
            return p1, p2
    return -1,-1

def test(array, target):
    answ1, answ2 = -1, -1
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]+array[j] == target:
                answ1,answ2 = i, j
                break
    print(answ1, answ2)
    return answ1, answ2


def main():
    for i in range(10):
        arr = []
        n = random.randint(2,10)
        targ = random.randint(1,10)
        for j in range(n):
            print(j)
            arr.append(random.randint(0,5))
        print(arr)
        arr = sorted(arr)


        print(f'arr={arr} targ={targ}\nsolution={solution(arr,targ)}') #\n')
        print('asdf')
        if solution(arr,targ)!=test(arr,targ):
            print(f'Error!\narr={arr} targ={targ}\ntest={test(arr,targ)}\nsolution={solution(arr,targ)}')
            return -1

    print('OK')
    return 0

main()





