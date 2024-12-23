import re

file = open("input.txt", "r")

input = file.readlines()

txt = ""
sum = 0

for row in input:
    txt = txt + row

pattern = r"mul\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)"

matches = re.finditer(pattern, txt)

results = []
counter = 0

do_not_found = False

for i in matches:
    
    start_pos = i.start()
    print(start_pos)
    print(txt[start_pos:])
    break
    before_match = txt[:start_pos]
    print(before_match)

    counter = counter + 1

    if counter == 30:
        break

    # Check if 'don't()' appears before the current 'mul'
    if "don't()" in before_match:
        print("this is met")
        do_not_found = True
    # If 'don't()' hasn't been found, check if 'do()' has appeared
    elif 'do()' in before_match or before_match == '':
        # If the conditions are met, add the match to results
        results.append(i.group(0))

#     num1 = int(i[0])
#     num2 = int(i[1])

#     result = num1 * num2

#     sum = sum + result

# print(sum)
print(results)