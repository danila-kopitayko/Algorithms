import random

def sol(array):
    l, m = 0,0
    while m<len(array):
        if array[m]%2==0:
            array[m],array[l] = array[l],array[m]
            m+=1
            l+=1
        else:
            m+=1
    return array

def main():
    n = random.randint(5,10)
    array = []
    for i in range(n):
        array.append(random.randint(0,10))
    print(array)
    print(sol(array))

main()
    
