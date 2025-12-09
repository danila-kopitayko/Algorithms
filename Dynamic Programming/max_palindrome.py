def test(string):
    n=len(string)
    max_length = 0
    for i in range(1,n-1):
        for j in range(2):
            l, r = i, i+j
            while l>=0 and r<n and string[l]==string[r]:
                l-=1
                r+=1
            if max_length<r-l-1:
                max_length = r - l - 1

    return max_length

def solution():
    


def main():
    s = 'babad'
    print(test(s))
    return 0


main()
