import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    queue = [(0,start)]
    while queue:
        curr_dist, curr = heapq.heappop(queue)

        if curr_dist>distances[curr]:
            continue

        for neighbour, weight in graph[curr].items():
            distance = curr_dist + weight

            if distance<distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(queue,(distance,neighbour))
    return distances


def main():
    g = {
    'A':{'B':1,'C':5},
    'B':{'A':1,'C':2,'D':3},
    'C':{'A':5,'B':2,'D':1},
    'D':{'B':3,'C':1}
    }
    print(dijkstra(g,'A'))
    return 0

main()