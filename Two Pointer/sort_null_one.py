def sol(array):
    p1, p2 = 0, len(array) - 1
    while p1 < p2:
        if array[p1] == 0:
            p1 += 1
        elif array[p2] == 1:
            p2 -= 1
        else:
            array[p1], array[p2] = array[p2], array[p1]
            p1 += 1
            p2 -= 1
    return array


def main():
    arr = [1, 1, 0, 1, 1, 0, 1, 1, 0]
    print(sol(arr))


main()
