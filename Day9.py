from shapely.geometry import Polygon, box

with open("9.txt") as f:
    lines = f.read().splitlines()

coords = [tuple(map(int, line.split(','))) for line in lines]

def getArea(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
    return (p1x - p2x + 1) * (p1y - p2y + 1)

def part_one():
    largest_area = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            area = getArea(coords[i], coords[j])
            if area > largest_area:
                largest_area = area
    print("Part 1:", largest_area)

def part_two():
    res = 0
    
    poly = Polygon(coords)
    
    for i in range(len(coords)):
        if i % 50 == 0:
            print(f"  Progress: {i}/{len(coords)}")
        
        a = coords[i]
        for j in range(len(coords)):
            if i == j:
                continue
            b = coords[j]
            
            minx = min(a[0], b[0])
            maxx = max(a[0], b[0])
            miny = min(a[1], b[1])
            maxy = max(a[1], b[1])
            
            rect = box(minx, miny, maxx, maxy)
            
            if rect.within(poly):
                area = (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)
                if area > res:
                    res = area
    
    print("Part 2:", res)

part_one()
part_two()
