ranges = []
items = []
with open("5.txt") as f:
    for line in f:
        if line.strip() == "":
            continue
        if "-" in line:
            ranges.append(line.strip())
        else:
            items.append(int(line.strip()))

def part_one():
    count = 0
    for i in items:
        for r in ranges:
            start, end = map(int, r.split("-"))
            if start <= i <= end:
                count += 1
                break
    print("Part 1:", count)

def part_two():
    parsed_ranges = []
    for r in ranges:
        start, end = map(int, r.split("-"))
        parsed_ranges.append((start, end))
    
    parsed_ranges.sort()
    merged = []
    for start, end in parsed_ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    total = sum(end - start + 1 for start, end in merged)
    print("Part 2:", total)

part_two()