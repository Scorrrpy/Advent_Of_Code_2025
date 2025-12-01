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
        delta = int(i)
        clicks, rotation = divmod(abs(delta), 100)
        carries += clicks
        
        if delta > 0:
            if value + rotation >= 100:
                carries += 1
            value = (value + rotation) % 100
        else:
            if value and value - rotation <= 0:
                carries += 1
            value = (value - rotation) % 100
        results.append(value)

    print("Part 2: " + str(carries))

part_one()
part_two()