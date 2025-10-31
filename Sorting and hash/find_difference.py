from collections import Counter

def solution(a,b):
    a=Counter(list(a))
    b=Counter(list(b))
    keys = list(a.keys())
    for value in keys:
        if value in b.keys():
            del a[value]
            del b[value]
    if b.keys():
        return list(b.keys())[0]
    else:
        return list(a.keys())[0]


def main():
    print(solution('aeadf','aadf'))
    return 0

main()