import random

def test(arr, k):
    cum_sum = [arr[0]]
    if len(arr)<k:
        return None

    for i in range(len(arr)-1):
        cum_sum.append(arr[i+1] + cum_sum[i])
    maxx = cum_sum[k-1]
    for i in range(k,len(arr)):
        if maxx<cum_sum[i] - cum_sum[i-k]:
            maxx = cum_sum[i] - cum_sum[i-k]
        #print(f'cum_sum[{i}]={cum_sum[i]} cum_sum[{i - k}]={cum_sum[i-k]}  max={maxx}')
    #print(f'cum_sum={cum_sum}')
    return maxx

def solution(arr,k):
    current_sum = 0

    for i in range(k):
        current_sum += arr[i]
    maxx = current_sum

    for i in range(k,len(arr)):
        #print(f'{arr[i - k]} {arr[i]} current_sum={current_sum}')
        current_sum = current_sum - arr[i-k] + arr[i]
        maxx = max(maxx,current_sum)
    return maxx





def main():
    n = 10
    arr = [random.randint(0,10) for i in range(n)]
    #arr = [6, 5, 5, 0, 8, 1, 0, 6, 3, 6]
    print(arr)
    print(solution(arr,5))
    print(test(arr,5))
    return 0


main()
