def sol(arr1,arr2):
    p1, p2 = 0, 0
    answ = []

    while p1<len(arr1) and p2<len(arr2):
        if arr1[p1] <= arr2[p2]:
            answ.append(arr1[p1])
            print('1',p1,arr1[p1])
            p1+=1

        else:
            answ.append(arr2[p2])
            print('2',p2,arr2[p2])
            p2+=1
    for i in range(len(arr1)-p1):
        answ.append(arr1[p1+i])
    for j in range(len(arr2)-p2):
        answ.append(arr2[p2+j])
    return answ


def main():
    array1=[1,3,5,8,10]
    array2 = [1,6,7]
    print(sol(array1,array2))

main()
