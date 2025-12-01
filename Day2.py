line = ""
with open ("2.txt", "r") as file:
    for l in file:
        line = l

ranges = line.strip().split(",")

def isValid(r, part2=False):
    if r.startswith("0"):
        return False
    if r.isdigit() == False:
        return False
    if len(r) % 2 == 0:
        mid = len(r) // 2
        if r[:mid] == r[mid:]:
            return False
    if part2:
        n = len(r)
        for length in range(1, n):
            if n % length == 0: 
                pattern = r[:length]
                if pattern * (n // length) == r:
                    return False
    return True

def part_one():
    invalid = []
    for r in ranges:
        t = r.split("-")
        for i in range(int(t[0]), int(t[1]) + 1):
            if not isValid(str(i)):
                invalid.append(i)

    sum = 0
    for i in invalid:
        sum += i

    print("Part 1: ", sum)

def part_two():
    invalid = []
    for r in ranges:
        t = r.split("-")
        for i in range(int(t[0]), int(t[1]) + 1):
            if not isValid(str(i), True):
                invalid.append(i)

    sum = 0
    for i in invalid:
        sum += i
    print("Part 2: ", sum)

part_one()
part_two()