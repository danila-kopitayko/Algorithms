def dfs(graph, node, visited, color):
    visited[node] = color
    for i in graph[node]:
        if visited[i] == 0:
            dfs(graph,i,visited,color)


def solution(g):
    visited = dict()

    for i in g:
        visited[i] = 0

    color = 0
    for i in g.keys():
        if visited[i] == 0:
            color+=1
            dfs(g,i,visited,color)
    return visited


def main():
    graph = {1:[2,3], 2:[1,3], 3:[1,2], 4:[6,7], 5:[6,7],6:[4,5,7],7:[4,5,6],8:[11],9:[10,11],10:[9],11:[8,9]}
    print(solution(graph))
    return 0

main()