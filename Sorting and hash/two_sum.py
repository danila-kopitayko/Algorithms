import random

def solution(data, target):
    for i in range(len(data)):
        diff = target-data[i]
        if diff in data:
            return [diff, data[i]]
    return []


def main():
    n = random.randint(2,10)
    arr =[0, 15, 14, 17, 10, 8, 14, 0, 0]
    for i in range(n):
        arr.append(random.randint(0,20))
    target = arr[random.randint(2,n-1)]+arr[1+random.randint(2,n-2)]
    print(arr,target)
    print(solution(arr,target))
    return 0

main()