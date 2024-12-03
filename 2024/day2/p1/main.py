row_list = []

file = open("input_small.txt", "r")

input_list = file.readlines()

for row in input_list:
    split_list = row.split()

    l1 = []

    # generates list with int's
    for i in split_list:
        l1.append(int(i))

    for i, j in enumerate(l1[:-1]):
        if j  == l1[i+1]: 
            print("smaller")

    print("----")