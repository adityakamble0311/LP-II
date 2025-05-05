import heapq

def prims(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (cost, node)
    total_cost = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        total_cost += cost
        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v))
    return total_cost

# Example Graph (Adjacency List)
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('D', 1)],
    'C': [('A', 3), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

print("Total cost of MST:", prims(graph, 'A'))
