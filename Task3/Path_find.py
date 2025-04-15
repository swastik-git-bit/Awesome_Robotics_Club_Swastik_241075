import heapq

grid_str = [
    "S....~..^.",
    "###..~#.^.",
    "...#..#...",
    ".~~#......",
    ".....####.",
    "^^....~~..",
    "#....#~~~.",
    "..##......",
    ".....^^^^G",
    ".######..."
]

tile_cost = {'S': 0,'G': 0,'.': 1,'~': 3,'^': 5,'#': float('inf')  }

grid = [list(row) for row in grid_str]
rows, cols = len(grid), len(grid[0])

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            start = (r, c)
        if grid[r][c] == 'G':
            goal = (r, c)

def dijkstra(start, goal):
    heap = [(0, start)]
    visited = set()
    cost_so_far = {start: 0}
    came_from = {start: None}

    while heap:
        cost, current = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            break

        for dr, dc in dirs:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                tile = grid[nr][nc]
                move_cost = tile_cost[tile]
                if move_cost == float('inf'):
                    continue  # Skip walls
                new_cost = cost + move_cost
                neighbor = (nr, nc)
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor))
                    came_from[neighbor] = current

    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from.get(node)
    path.reverse()
    return path, cost_so_far.get(goal, float('inf'))

path, total_cost = dijkstra(start, goal)

print("Least costly path:")
for r, c in path:
    print(f"({r},{c}) -> ", end="")
print("GOAL")
print(f"Total cost: {total_cost}")

