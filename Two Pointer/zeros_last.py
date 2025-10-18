import random


def solution(arr):
    curr, l = len(arr) - 1, len(arr) - 1

    while curr >= 0:
        if arr[curr] == 0:
            arr[curr], arr[l] = arr[l], arr[curr]
            curr -= 1
            l -= 1
        else:
            curr -= 1
    return arr


def main():
    n = random.randint(3, 10)
    n_zeros = random.randint(1, n)
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10))

    for i in range(n_zeros):
        arr.insert(random.randint(0, n - 1), 0)

    print(arr)
    print(solution(arr))


main()
