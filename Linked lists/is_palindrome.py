import random

def solution(word):
    deque = list(word)
    left = 0
    right = len(word) - 1
    while left<right:
        if deque[left]!=deque[right]:
            return False
        left+=1
        right-=1
    return True


def main():
    n = random.randint(2,5)

    half1 = []
    half2 = []
    for i in range(n):
        half1.append(str(random.randint(0,9)))

    half2 = half1[::-1]

    palindrome = ''.join(half1) + ''.join(half2)
    print(palindrome)
    print(solution(palindrome))

main()
