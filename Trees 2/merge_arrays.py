from Tree2 import heap_sort
import heapq

def merge_arrays(arr):
    res = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            res.append(arr[i][j])
    merged_array = []

    heap = heap_sort(res)

    for i in range(len(heap)):
        merged_array.append(heap[i].data)
    return merged_array

def merge_arrays_fast(arr):
    n = len(arr)
    merged = []
    heap = []
    for i in range(n):
        curr = arr[i]
        if len(arr[i])>0:
            heapq.heappush(heap,(curr[0],i,0))
    while heap:
        val, arr_idx, val_idx = heapq.heappop(heap)
        merged.append(val)
        if val_idx + 1< len(arr[arr_idx]):
            next_el = arr[arr_idx][val_idx + 1]
            heapq.heappush(heap,(next_el,arr_idx,val_idx + 1))
    return merged








def main():
    arr = [[1,4,5], [1,3,4], [2,6]]
    print('arr:',arr)

    solution = merge_arrays(arr)

    print(solution)

    solution2 = merge_arrays_fast(arr)

    print(solution2)

    return 0


main()