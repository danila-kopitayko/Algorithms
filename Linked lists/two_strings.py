import random
import string




def solution(string1: str, string2: str):
    if len(string1)>len(string2):
        l = list(string1)
        s = list(string2)
    else:
        l = list(string2)
        s = list(string1)
    q = []
    for el in s:
        q.append(el)

    for el in l:
        #print(el)
        if q and q[0] == el:
            q.pop(0)
        if not q:
            return True
    return len(q)==0


def main():
    characters = string.ascii_letters
    str1 = ''.join(random.choices(characters,k=10))
    n = random.randint(3,10)
    arr = random.sample(range(0, n), n)
    arr.sort()
    #str1 = ''.join(random.choices(characters, k=10))
    str2 = ''
    for i in range(n):
        str2+=str1[arr[i]]
    print(list(str1))
    print(list(str2))
    print(solution(str1,str2))


main()

