import heapq

with open("8.txt") as f:
    lines = f.read().splitlines()

points = [tuple(map(int, line.split(','))) for line in lines]

def distance(p1, p2):
    return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return True
    
    def get_sizes(self):
        groups = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            groups[root] = groups.get(root, 0) + 1
        return sorted(groups.values(), reverse=True)

def part_one():
    n = len(points)
    distances = []
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            distances.append((dist, i, j))
    
    distances.sort()
    
    uf = UnionFind(n)
    
    for k in range(min(1000, len(distances))):
        _, i, j = distances[k]
        uf.union(i, j)
    
    sizes = uf.get_sizes()
    if len(sizes) >= 3:
        result = sizes[0] * sizes[1] * sizes[2]
        print("Part 1:", result)
    else:
        print(f"Part 1: Only {len(sizes)} circuits found")

def part_two():
    n = len(points)
    distances = []
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            distances.append((dist, i, j))
    
    distances.sort()
    
    uf = UnionFind(n)
    
    last_i, last_j = 0, 0
    for dist, i, j in distances:
        if uf.union(i, j):
            last_i, last_j = i, j
            sizes = uf.get_sizes()
            if len(sizes) == 1:
                break
    
    result = points[last_i][0] * points[last_j][0]
    print("Part 2:", result)

part_one()
part_two()
