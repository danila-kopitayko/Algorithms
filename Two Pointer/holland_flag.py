def sol(array):
    l,m=0,0
    h=len(array)-1

    while m<=h:
        if array[m]==0:
            array[l],array[m] = array[m], array[l]
            m+=1
            l+=1
        elif array[m]==1:
            m+=1
        elif array[m]==2:
            array[h],array[m] = array[m], array[h]
            h-=1
    return array


def main():

    arr = [1,1,2,0,2,1,2]

    print(sol(arr))

main()
