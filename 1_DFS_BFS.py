def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited, graph, start_node):
    queue = [start_node]
    visited.add(start_node)

    while queue:
        current = queue.pop(0)
        print(current, end=" ")
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [],
        5: [],
        6: [],
        7: []
    }

    print("DFS Traversal:")
    dfs(set(), graph, 1)

    print("\nBFS Traversal:")
    bfs(set(), graph, 1)

if __name__ == "__main__":
    main()



# With User Input code : 


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph.get(node, []):
            dfs(visited, graph, neighbour)

def bfs(visited, graph, start_node):
    queue = [start_node]
    visited.add(start_node)

    while queue:
        current = queue.pop(0)
        print(current, end=" ")
        for neighbour in graph.get(current, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    graph = {}
    n = int(input("Enter number of nodes: "))

    for i in range(1, n + 1):
        node = str(i)
        edges = input(f"Enter neighbors of node {node} : ").split()
        graph[node] = edges

    start = input("Enter starting node for traversal: ")

    print("\nDFS Traversal:")
    dfs(set(), graph, start)

    print("\nBFS Traversal:")
    bfs(set(), graph, start)

if __name__ == "__main__":
    main()

