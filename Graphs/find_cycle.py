def dfs(graph, vertex, parent, visited):
    visited[vertex] = True
    for i in graph[vertex]:
        if i!=parent:
            if visited[i] or dfs(graph,i,vertex,visited):
                return True
    return False


def solution(g):
    visited = dict()

    for i in g.keys():
        visited[i]=False
    for i in g.keys():
        if visited[i] is False:
            if dfs(g,i,None,visited):
                return True
    return False


def main():
    g = {1:[2],2:[1,3],3:[2,4],4:[3]}
    print(solution(g))



    return 0

main()