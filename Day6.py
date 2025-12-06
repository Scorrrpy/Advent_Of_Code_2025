with open("6.txt") as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

def get_problems():
    max_len = max(len(line) for line in lines)
    problems = []
    start = 0
    
    for col in range(max_len):
        is_separator = all(col >= len(row) or row[col] == ' ' for row in lines)
        
        if is_separator and col > start:
            problems.append((start, col))
            start = col + 1
    
    if start < max_len:
        problems.append((start, max_len))
    
    return problems

def calculate(numbers, operator):
    result = numbers[0]
    for num in numbers[1:]:
        result = result + num if operator == '+' else result * num
    return result

def part_one():
    total = 0
    for start_col, end_col in get_problems():
        numbers, operator = [], None
        
        for row in lines:
            text = row[start_col:end_col].strip() if start_col < len(row) else ""
            if text in ['+', '*']:
                operator = text
            elif text.isdigit():
                numbers.append(int(text))
        
        if numbers and operator:
            total += calculate(numbers, operator)
    
    print("Part 1:", total)

def part_two():
    total = 0
    for start_col, end_col in get_problems():
        numbers, operator = [], None
        
        for col in range(end_col - 1, start_col - 1, -1):
            digits = []
            for row in lines:
                if col < len(row) and row[col] != ' ':
                    if row[col] in ['+', '*']:
                        operator = row[col]
                    elif row[col].isdigit():
                        digits.append(row[col])
            
            if digits:
                numbers.append(int(''.join(digits)))
        
        if numbers and operator:
            total += calculate(numbers, operator)
    
    print("Part 2:", total)

part_one()
part_two()
    
