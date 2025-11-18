class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right


def solution(data):
    if len(data)<=3:
        return -1
    min_idx = 1
    max_idx = 2
    i = 0
    while True:
        min_idx_buff = 2 * i + 1
        if min_idx_buff < len(data):
            min_idx = min_idx_buff
            i = min_idx_buff
            continue
        break

    while True:
        max_idx_buff = 2 * i + 2
        if min_idx_buff < len(data):
            max_idx = max_idx_buff
            i = max_idx_buff
            continue
        break
    return data[max_idx] * data[min_idx]

def main():
    return 0


main()