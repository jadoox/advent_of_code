row_list = []

file = open("input.txt", "r")

input_list = file.readlines()

safe_count = 0

for row in input_list:
    split_list = row.split()

    l1 = []

    for i in split_list:
        l1.append(int(i))

    fail_count = 0
    is_increasing = 0
    is_decreasing = 0

    for i in range(len(l1) - 1):
        current = l1[i]
        next_item = l1[i + 1]
        
        diff = next_item - current

        if fail_count > 1:
            break

        if diff > 0:
            if is_decreasing > 0:
                fail_count = fail_count + 1
            is_increasing = is_increasing + 1

        if diff < 0:
            if is_increasing > 0:
                fail_count = fail_count + 1
            is_decreasing = is_decreasing + 1

        if abs(diff) < 1 or abs(diff) > 3 or abs(diff) == 0:
            fail_count = fail_count + 1
            continue
            
    if fail_count < 2:
        print(l1)
        safe_count = safe_count + 1

    print("----")


print(safe_count)