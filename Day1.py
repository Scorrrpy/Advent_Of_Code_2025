sol = []
with open("1.txt") as f:
    for l in f:
        if "L" in l:
            sol.append(l.replace("L", "-"))
        if "R" in l:
            sol.append(l.replace("R", ""))

def part_one():
    value = 50
    results = []
    for i in sol:
        value = (value + int(i)) % 100
        results.append(value)

    highest_val = 0
    for i in results:
        temp = results.count(i)
        if (temp > highest_val):
            highest_val = temp
        
    print("Part 1: " + str(highest_val))

def part_two():
    value = 50
    carries = 0
    results = []
    for i in sol:
        value += int(i)
        wraps = abs(value) // 100
        carries += wraps
        value = value % 100
        results.append(value)

    zeros = results.count(0)
    total = carries + zeros
    print("Part 2: " + str(total))

part_one()
part_two()