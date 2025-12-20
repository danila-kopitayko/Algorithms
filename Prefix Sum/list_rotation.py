def test(arr):
    ptr1, ptr2 = 1, len(arr) - 2
    cum_sum1, cum_sum2 = arr[0], arr[len(arr) - 1]

    while ptr1 < ptr2:
        if cum_sum1>cum_sum2:
            cum_sum2 += arr[ptr2]
            ptr2-=1
        else:
            cum_sum1 += arr[ptr1]
            ptr1+=1
        #print(f'cum_sum1={cum_sum1}\ncum_sum2={cum_sum2}')
        if cum_sum1==cum_sum2:
            #print(cum_sum1)
            if ptr1==ptr2:
                return ptr1
    return None

def solution(arr):
    summ = sum(arr)
    left = 0

    for i in range(len(arr)):
        if left == summ - left - arr[i]:
            return i
        left+=arr[i]
    return None

def main():
    arr = [9,4,8,7,1,11,2,6,1]
    print(test(arr))
    print(solution(arr))

    return 0


main()