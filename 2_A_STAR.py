from queue import PriorityQueue

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) 

def astar(grid, start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g = {start: 0}

    while not open_set.empty():
        _, current = open_set.get()
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = current[0]+dx, current[1]+dy
            neighbor = (nx, ny)
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                temp_g = g[current] + 1
                if neighbor not in g or temp_g < g[neighbor]:
                    g[neighbor] = temp_g
                    f = temp_g + heuristic(neighbor, goal)
                    open_set.put((f, neighbor))
                    came_from[neighbor] = current
    return None

# Example usage
grid = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [1,1,0,0,0]
]
start = (0,0)
goal = (3,4)

print("Path:", astar(grid, start, goal))
