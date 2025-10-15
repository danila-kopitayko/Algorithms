def swap(arr,left,right):
    while left<right:
        arr[left],arr[right] = arr[right], arr[left]
        left+=1
        right-=1
    return arr

def solution(arr,index):
    arr = swap(arr, 0, len(arr) - 1)
    arr = swap(arr,0,index-1)
    arr = swap(arr,index,len(arr)-1)
    return arr



def main():
    print(swap([1,2,3,4,5,6,7],0,3))

    print(solution([1,2,3,4,5,6,7],3))


main()

