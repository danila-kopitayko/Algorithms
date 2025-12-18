def solution(nums, k):
    prefix_sum = 0
    count = 0
    prefix_count = dict()
    prefix_count[0] = 1

    for num in nums:
        prefix_sum += num
        #print(prefix_sum)
        if prefix_sum - k in prefix_count.keys():
            #print('before',count)
            count += prefix_count[prefix_sum - k]
            #print('after',count)
        if prefix_sum in prefix_count.keys():
            prefix_count[prefix_sum]=prefix_count[prefix_sum]+1
        else:
            prefix_count[prefix_sum]=1
        #print(prefix_count)
    return count


def main():
    arr = [3,8,6,9,2,1,4]

    print(solution(arr,11))


    return 0

main()
