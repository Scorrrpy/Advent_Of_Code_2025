import re
from itertools import combinations

with open("10.txt") as f:
    lines = f.read().splitlines()


def parse_line(line):
    lights_match = re.search(r'\[([.#]+)\]', line)
    lights = lights_match.group(1)
    target = [1 if c == '#' else 0 for c in lights]

    buttons = []
    for match in re.finditer(r'\(([0-9,]+)\)', line):
        buttons.append([int(x) for x in match.group(1).split(',')])

    joltage_match = re.search(r'\{([0-9,]+)\}', line)
    joltage = [int(x) for x in joltage_match.group(1).split(',')]

    return target, buttons, joltage


def find_min_presses_bruteforce(target, buttons):
    n_lights = len(target)
    n_buttons = len(buttons)
    for k in range(n_buttons + 1):
        for combo in combinations(range(n_buttons), k):
            state = [0] * n_lights
            for btn_idx in combo:
                for light_idx in buttons[btn_idx]:
                    state[light_idx] ^= 1
            if state == target:
                return k
    return -1


def find_min_presses_gaussian(target, buttons):
    n_eq = len(target)
    n_vars = len(buttons)
    matrix = []
    for i in range(n_eq):
        row = [1 if i in button else 0 for button in buttons]
        matrix.append(row + [target[i]])

    pivot_cols = []
    row_idx = 0
    for col in range(n_vars):
        pivot = None
        for r in range(row_idx, n_eq):
            if matrix[r][col] == 1:
                pivot = r
                break
        if pivot is None:
            continue
        if pivot != row_idx:
            matrix[row_idx], matrix[pivot] = matrix[pivot], matrix[row_idx]
        for r in range(n_eq):
            if r != row_idx and matrix[r][col] == 1:
                for c in range(n_vars + 1):
                    matrix[r][c] ^= matrix[row_idx][c]
        pivot_cols.append(col)
        row_idx += 1
        if row_idx >= n_eq:
            break

    for r in range(row_idx, n_eq):
        if matrix[r][n_vars] == 1:
            return -1

    free_vars = [i for i in range(n_vars) if i not in pivot_cols]
    best = n_vars + 1
    for mask in range(1 << len(free_vars)):
        solution = [0] * n_vars
        for i, var in enumerate(free_vars):
            solution[var] = (mask >> i) & 1
        for i in range(len(pivot_cols) - 1, -1, -1):
            col = pivot_cols[i]
            val = matrix[i][n_vars]
            for j in range(col + 1, n_vars):
                val ^= matrix[i][j] & solution[j]
            solution[col] = val
        presses = sum(solution)
        if presses < best:
            best = presses

    return best if best <= n_vars else -1


def part_one():
    total = 0
    for line in lines:
        target, buttons, _ = parse_line(line)
        min_presses = find_min_presses_gaussian(target, buttons)
        total += min_presses
    print(f"Part 1: {total}")


def solve_joltage(target, buttons):
    import pulp
    
    n_counters = len(target)
    n_buttons = len(buttons)
    
    prob = pulp.LpProblem("JoltageConfig", pulp.LpMinimize)
    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat='Integer') for i in range(n_buttons)]
    prob += pulp.lpSum(x)
    
    for j in range(n_counters):
        prob += pulp.lpSum([x[i] for i in range(n_buttons) if j in buttons[i]]) == target[j]
    
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    
    if prob.status != pulp.LpStatusOptimal:
        return -1
    
    total_presses = sum(int(var.varValue) for var in x)
    return total_presses

def part_two():
    total = 0
    for line in lines:
        _, buttons, joltage = parse_line(line)
        min_presses = solve_joltage(joltage, buttons)
        total += min_presses
    print(f"Part 2: {total}")


part_one()
part_two()
