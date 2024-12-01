row1 = []
row2 = []

num_list1 = []
num_list2 = []

similarity = []

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

for i1 in num_list1:
    count = 0
    for i2 in num_list2:
        if i2 == i1:
          count = count + 1

    if count != 0:
        similarity.append(i1 * count)

print(sum(similarity))