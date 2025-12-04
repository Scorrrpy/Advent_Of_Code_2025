with open("4.txt", "r") as file:
    grid = [list(line.strip()) for line in file.readlines()]

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]

def count_neighbors(r, c):
    neighbors = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
            neighbors += 1
    return neighbors

def part_one():
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                if count_neighbors(r, c) < 4:
                    count += 1
    print("Part 1:", count)

def part_two():
    grid_copy = [row[:] for row in grid]
    total_removed = 0
    
    while True:
        to_remove = []
        for r in range(rows):
            for c in range(cols):
                if grid_copy[r][c] == '@':
                    neighbors = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid_copy[nr][nc] == '@':
                            neighbors += 1
                    if neighbors < 4:
                        to_remove.append((r, c))
        
        if not to_remove:
            break
        
        for r, c in to_remove:
            grid_copy[r][c] = '.'
        total_removed += len(to_remove)
    
    print("Part 2:", total_removed)

part_one()
part_two()