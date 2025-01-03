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
condition = ""

for i in matches:
    start_pos = i.start()

    before_match = txt[:start_pos]

    for ch in range(len(before_match)):
        if before_match[ch:ch+7] == "don't()":
            condition = "don't"
        if before_match[ch:ch+4] == "do()":
            condition = "do"

    if condition == "do":
        num1 = int(i.group(1))
        num2 = int(i.group(2))

        result = num1 * num2

        sum = sum + result

print(sum)