def swap(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def solution(arr, index):
    n = len(arr)
    arr = swap(arr, 0, n - 1)
    arr = swap(arr, 0, index % n - 1)
    arr = swap(arr, index % n, n - 1)
    return arr


def main():
    print(swap([1, 2, 3, 4, 5, 6, 7], 0, 3))

    print(solution([1, 2, 3, 4, 5, 6, 7], 3))


main()
