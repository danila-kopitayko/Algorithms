def dfs(graph, node, visited, component):
    visited[node] = True
    component.append(node)
    for i in graph[node]:
        if visited[i] is False:
            dfs(graph,i,visited,component)



def solution(g):
    visited = dict()
    connected_components = []
    for i in g:
        visited[i] = False
    for i in g.keys():
        if visited[i] is False:
            components = []
            dfs(g,i,visited,components)
            connected_components.append(components)
    return len(connected_components)



def main():
    graph = {1:[2,3], 2:[1,3], 3:[1,2], 4:[6,7], 5:[6,7],6:[4,5,7],7:[4,5,6],8:[11],9:[10,11],10:[9],11:[8,9]}
    print(solution(graph))
    return 0

main()