def is_tree(graph,start):
    visited = []
    queue = [start]
    parents = dict()
    parents[start] = None

    while queue:
        curr = queue.pop(0)
        visited.append(curr)

        for i in graph[curr]:
            if i not in visited:
                queue.append(i)
                parents[i] = curr
            else:
                if i not in parents.values():
                    return False
    return len(visited)==len(graph)


def main():
    g = {'A':['B','C','D'],'B':['A'],'C':['A'],'D':['A','F','E'],'F':['D'],'E':['D']}
    print(is_tree(g,'A'))
    return 0

main()