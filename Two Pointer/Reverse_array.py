import random
def solution(array):
    n = len(array)
    p1, p2 = 0, n - 1
    buff = 0
    #print(array)
    while p1!=n//2:
        #print(p1, array[p1])
        buff = array[p1]
        array[p1] = array[p2]
        array[p2] = buff
        p1+=1
        p2-=1
    return array

def test(array):
    array_rev = array[::-1]
    return array_rev

def main():
    for k in range(5):
        n = random.randint(2,10)
        arr = []
        for i in range(n):
            arr.append(random.randint(0,100))
        #print(f'arr={arr}\ntest={test(arr)}\nsolution={solution(arr)}')

        if test(arr)!=solution(arr):
            print(f'Error!\narr={arr}\ntest(arr)={test(arr)}\nsolution={solution(arr)}')
            return -1
    print('OK!')
    return 0





main()

