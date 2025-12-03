with open("3.txt", "r") as file:
    lines = file.readlines()


def part_one():
    max_values_by_line = []
    for line in lines:
        max_temp = 0
        max_temp_index = -1
        for index, digit in enumerate(line.strip()):
            if not index == len(line.strip()) - 1:
                if int(digit) > max_temp:
                    max_temp = int(digit)
                    max_temp_index = index
        max_2 = 0
        for i in range(max_temp_index +1, len(line.strip())):
            if int(line.strip()[i]) > max_2:
                max_2 = int(line.strip()[i])
        max_values_by_line.append(str(max_temp) + "" + str(max_2))

    sum = 0
    for val in max_values_by_line:
        print(val)
        sum += int(val)
    print("Part 1: " + str(sum))
            

def part_two():
    def max_number_by_removing(s, keep):
        to_remove = len(s) - keep
        stack = []
        for digit in s:
            while to_remove > 0 and stack and digit > stack[-1]:
                stack.pop()
                to_remove -= 1
            stack.append(digit)

        while to_remove > 0:
            stack.pop()
            to_remove -= 1
        
        return ''.join(stack)
    
    total = 0
    for line in lines:
        result = max_number_by_removing(line.strip(), 12)
        total += int(result)
    print("Part 2: " + str(total))


part_one()
part_two()



