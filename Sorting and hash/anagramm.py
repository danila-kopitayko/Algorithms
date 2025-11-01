import random
from collections import Counter

global total_letters

total_letters = 26

def hash(word):
    key = [0]*26
    hash = []
    for i in range(len(word)):
        key[ord(word[i])-ord('a')]+=1
    for i in range(total_letters):
        hash.append(str(key[i]))
        hash.append('|')

    return ''.join(hash)


def solution(array):
    d = dict()
    for i in range(len(array)):
        hash_arr = hash(array[i])
        if  hash_arr not in list(d.keys()):
            d[hash_arr] = []
        d[hash_arr].append(array[i])
    return list(d.values())

def test(array):
    d = dict()
    for i in range(len(array)):
        d["".join(sorted(array[i]))] = []
    for i in range(len(array)):
        d["".join(sorted(array[i]))].append(array[i])
    return list(d.values())

def main():
    array = ['eat','tea','tan','ate','nat','bat']
    print(test(array))
    print(solution(array))
    return 0

main()