def solution(arr):
    prefix_sum = 0
    maxx = 0
    index_map = dict()
    index_map[0] = -1

    for i in range(len(arr)):
        num = arr[i]
        prefix_sum = prefix_sum + 1 if num==1 else prefix_sum - 1

        if prefix_sum in index_map.keys():
            maxx = max(maxx, i - index_map[prefix_sum])
        else:
            index_map[prefix_sum] = i
    return maxx




def main():
    arr=[-1,1,-1]

    print(solution(arr))

    return 0

main()