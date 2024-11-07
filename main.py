from queue import PriorityQueue
import time

grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
]

start = (0, 0)
goal = (4, 4)

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy_best_first_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = PriorityQueue()
    open_set.put((manhattan_distance(start, goal), start))
    came_from = {}
    visited = set()
    visited.add(start)
    
    while not open_set.empty():
        _, current = open_set.get()
        
        if current == goal:
            return reconstruct_path(came_from, start, goal)
        
        for neighbor in get_neighbors(current, rows, cols, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                open_set.put((manhattan_distance(neighbor, goal), neighbor))

    return None

def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}
    visited = set()
    
    while not open_set.empty():
        _, current = open_set.get()
        
        if current == goal:
            return reconstruct_path(came_from, start, goal)
        
        for neighbor in get_neighbors(current, rows, cols, grid):
            tentative_g_score = g_score[current] + 1
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + manhattan_distance(neighbor, goal)
                open_set.put((f_score, neighbor))
                visited.add(neighbor)
    
    return None

def get_neighbors(position, rows, cols, grid):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for d in directions:
        neighbor = (position[0] + d[0], position[1] + d[1])
        if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
            neighbors.append(neighbor)
    
    return neighbors

def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from.get(current)
        if current is None:
            return None
    path.append(start)
    path.reverse()
    return path

if __name__ == "__main__":
    start_time = time.time()
    path_greedy = greedy_best_first_search(grid, start, goal)
    time_greedy = time.time() - start_time
    print("Greedy Best-First Search")
    print("Path found - ", path_greedy)
    print("Time taken - {:.6f} seconds".format(time_greedy))
    
    start_time = time.time()
    path_a_star = a_star_search(grid, start, goal)
    time_a_star = time.time() - start_time
    print("A* Search")
    print("Path found - ", path_a_star)
    print("Time taken - {:.6f} seconds".format(time_a_star))
    
    print("\nEfficiency Comparison:")
    print("Greedy Best-First Search took {:.6f} seconds".format(time_greedy))
    print("A* Search took {:.6f} seconds".format(time_a_star))
    
    print("\nPath Quality Comparison:")
    print("Length of path found by Greedy:", len(path_greedy) if path_greedy else "No path found")
    print("Length of path found by A*:", len(path_a_star) if path_a_star else "No path found")