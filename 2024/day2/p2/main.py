row_list = []

file = open("input.txt", "r")

input_list = file.readlines()

safe_count = 0

for row in input_list:
    split_list = row.split()

    l1 = []

    for i in split_list:
        l1.append(int(i))

    alternate_lists = []

    for i in range(len(l1)):
        new_list = l1[:i] + l1[i+1:]
        alternate_lists.append(new_list)

    alt_safe = 0

    for list in alternate_lists:
        fail = False
        is_increasing = 0
        is_decreasing = 0

        for num in range(len(list) - 1):
            current = list[num]
            next_item = list[num + 1]
            
            diff = next_item - current

            if diff > 0:
                if is_decreasing > 0:
                    fail = True
                    break
                is_increasing = is_increasing + 1

            if diff < 0:
                if is_increasing > 0:
                    fail = True
                    break
                is_decreasing = is_decreasing + 1

            if abs(diff) < 1 or abs(diff) > 3 or abs(diff) == 0:
                fail = True
                break
                
        if fail == False:
            alt_safe = alt_safe + 1

    if alt_safe > 0:
        safe_count = safe_count + 1

print(safe_count)