row1 = []
row2 = []

num_list1 = []
num_list2 = []

distances = []

file = open("input.txt", "r")

input_list = file.readlines()

for row in input_list:
    line = row.replace(" ", "")

    row1.append(line[:5].replace("\n", ""))
    row2.append(line[5:].replace("\n", ""))

for s in row1:
    num = int(s)
    num_list1.append(num)

for s in row2:
    num = int(s)
    num_list2.append(num)

num_list1.sort()
num_list2.sort()

for f, b in zip(num_list1, num_list2):
    if f > b:
        su = f - b
    else:
        su = b - f

    distances.append(su)

print(sum(distances))