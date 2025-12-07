with open("7.txt") as f:
    grid = [line.strip() for line in f.readlines()]

def part_one():
    start_col = grid[0].index('S')
    
    active_beams = {start_col}
    splits = 0
    
    for row in range(1, len(grid)):
        next_beams = set()
        
        for col in active_beams:
            if grid[row][col] == '^':
                splits += 1
                if col > 0:
                    next_beams.add(col - 1)
                if col < len(grid[0]) - 1:
                    next_beams.add(col + 1)
            else:
                next_beams.add(col)
        
        active_beams = next_beams
        if not active_beams:
            break
    
    print("Part 1:", splits)

def part_two():
    start_col = grid[0].index('S')
    
    from collections import defaultdict
    paths_at_col = defaultdict(int)
    paths_at_col[start_col] = 1
    
    for row in range(1, len(grid)):
        next_paths = defaultdict(int)
        
        for col, count in paths_at_col.items():
            if grid[row][col] == '^':
                if col > 0:
                    next_paths[col - 1] += count
                if col < len(grid[0]) - 1:
                    next_paths[col + 1] += count
            else:
                next_paths[col] += count
        
        paths_at_col = next_paths
        if not paths_at_col:
            break
    
    print("Part 2:", sum(paths_at_col.values()))

part_one()
part_two()