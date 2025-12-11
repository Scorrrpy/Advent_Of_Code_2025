with open("11.txt") as f:
    lines = f.read().splitlines()

graph = {}
for line in lines:
    parts = line.split(': ')
    device = parts[0]
    outputs = parts[1].split()
    graph[device] = outputs

def count_paths(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    
    if start == end:
        return 1
    
    visited.add(start)
    
    total_paths = 0
    
    if start in graph:
        for neighbor in graph[start]:
            if neighbor not in visited:
                total_paths += count_paths(graph, neighbor, end, visited)
    
    visited.remove(start)
    
    return total_paths

def count_paths_with_required_memo(graph, device, has_dac, has_fft, memo):
    key = (device, has_dac, has_fft)
    if key in memo:
        return memo[key]
    
    count = 0
    
    if device in graph:
        for neighbor in graph[device]:
            if neighbor != "out":
                new_has_dac = has_dac or (neighbor == "dac")
                new_has_fft = has_fft or (neighbor == "fft")
                count += count_paths_with_required_memo(graph, neighbor, new_has_dac, new_has_fft, memo)
            else:
                if has_dac and has_fft:
                    count += 1
    
    memo[key] = count
    return count

def part_one():
    print(f"Part 1: {count_paths(graph, 'you', 'out')}")

def part_two():
    memo = {}
    result = count_paths_with_required_memo(graph, 'svr', False, False, memo)
    print(f"Part 2: {result}")

part_one()
part_two()