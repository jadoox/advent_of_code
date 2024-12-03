row_list = []

file = open("input.txt", "r")

input_list = file.readlines()

safe_count = 0

for row in input_list:
    split_list = row.split()

    l1 = []

    for i in split_list:
        l1.append(int(i))

    is_increasing = True
    is_decreasing = True

    for i in range(len(l1) - 1):
        current = l1[i]
        next_item = l1[i + 1]
        
        diff = next_item - current
        
        if abs(diff) < 1 or abs(diff) > 3:
            is_increasing = is_decreasing = False
            break
        
        if diff > 0:
            is_decreasing = False
        elif diff < 0:
            is_increasing = False

    if (is_increasing or is_decreasing) and (len(l1) > 1):
        safe_count = safe_count + 1

print(safe_count)