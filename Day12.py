with open("12.txt") as f:
    data = f.read()

*shapes, regions = data.split("\n\n")
shapes = [s.count("#") for s in shapes]

count = 0
for region in regions.strip().split("\n"):
    size, quants = region.split(": ")
    area = eval(size.replace("x", "*"))
    quants = eval(quants.replace(" ", ","))
    total = sum(a * b for a, b in zip(quants, shapes))
    if total < area:
        count += 1

print(f"Total Regions: {count}")

