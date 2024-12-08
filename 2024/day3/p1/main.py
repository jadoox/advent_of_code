import re

file = open("input.txt", "r")

input = file.readlines()

txt = ""
sum = 0

for row in input:
    txt = txt + row

pattern = r"mul\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)"

matches = re.findall(pattern, txt)

for i in matches:
    num1 = int(i[0])
    num2 = int(i[1])

    result = num1 * num2

    sum = sum + result

print(sum)