import time

previous = 0
current = 0
Total_Part_1 = 0
Total_Part_2 = 0
numbers = []
part2_nums = []
with open('input.txt', 'r') as file:
        for line in (file.readlines()):
            stripline = (line.strip('\n'))
            numbers.append(int(stripline))

        current = numbers[0]
        for i in range(1, len(numbers)):
            previous = current
            current = numbers[i]
            if (current - previous) > 0:
                Total_Part_1 += 1
print("=====================")
print("Total Part 1: " + str(Total_Part_1-1))
part2_nums = [numbers[0], numbers[1], numbers[2]]
current  = part2_nums[0] + part2_nums[1] + part2_nums[2]
for i in range(3, len(numbers)):
    previous = current
    part2_nums.pop(0)
    part2_nums.append(numbers[i])
    current = part2_nums[0] + part2_nums[1] + part2_nums[2]
    if (current - previous) > 0:
        Total_Part_2 += 1
print("=====================")
print("Total Part 1: " + str(Total_Part_1))
print("Total Part 2: " + str(Total_Part_2))