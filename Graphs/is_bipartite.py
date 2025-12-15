def bfs(graph, vertex):
    queue = [vertex]
    visited = []
    colors = dict()
    color = 0
    colors[vertex] = color
    while queue:
        curr = queue.pop(0)
        visited.append(curr)
        for i in graph[curr]:
            if i not in visited:
                colors[i]=(colors[curr]+1)%2
                queue.append(i)
            elif colors[i]==colors[curr]:
                return False
    return True

def dfs(graph, vertex,visited,colors,c):
    visited.append(vertex)
    colors[vertex]=c
    for i in graph[vertex]:
        if i not in visited:
            c=(c+1)%2
            dfs(graph,i,visited,colors,c)
        elif colors[i]==colors[vertex]:
            return False
    return True

def main():
    g1 = {1:[2,6],2:[1,3],3:[2,4],4:[3,5],5:[4,6],6:[5,1]}
    g2 = {1: [2, 5], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 1]}
    print(bfs(g2,1))

    colors = dict()
    c=0
    visited=[]
    print(dfs(g2,1,visited,colors,c))
    return 0


main()