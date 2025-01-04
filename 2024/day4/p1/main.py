row_list = []

file = open("input.txt", "r")

input_list = file.readlines()

match = 0

for row_num in range(len(input_list)):    
    row = input_list[row_num]
    for ch in range(len(row)):
        # Horizontal
        if row[ch:ch+4] == "XMAS":
            print("found XMAS")
            match = match + 1
        if row[ch:ch+4] == "SAMX":
            print("found SAMX")
            match = match + 1

        if row[ch] == "X":
            # Vertical
            if len(input_list) > row_num+1 and input_list[row_num+1][ch] == "M":
                if len(input_list) > row_num+2 and input_list[row_num+2][ch] == "A":
                    if len(input_list) > row_num+3 and input_list[row_num+3][ch] == "S":
                        print("found XMAS vertical")
                        match = match + 1
            # Diagonal
            if ch < 3: # check only right
                if len(input_list) > row_num+1 and input_list[row_num+1][ch+1] == "M":
                    if len(input_list) > row_num+2 and input_list[row_num+2][ch+2] == "A":
                        if len(input_list) > row_num+3 and input_list[row_num+3][ch+3] == "S":
                            print("found XMAS right diagonal")
                            match = match + 1
            elif ch > 136: # check only left
                if len(input_list) > row_num+1 and input_list[row_num+1][ch-1] == "M":
                    if len(input_list) > row_num+2 and input_list[row_num+2][ch-2] == "A":
                        if len(input_list) > row_num+3 and input_list[row_num+3][ch-3] == "S":
                            print("found XMAS right diagonal")
                            match = match + 1
            else:
                # check right
                if len(input_list) > row_num+1 and input_list[row_num+1][ch+1] == "M":
                    if len(input_list) > row_num+2 and input_list[row_num+2][ch+2] == "A":
                        if len(input_list) > row_num+3 and input_list[row_num+3][ch+3] == "S":
                            print("found XMAS right diagonal")
                            match = match + 1
                # check left
                if len(input_list) > row_num+1 and input_list[row_num+1][ch-1] == "M":
                    if len(input_list) > row_num+2 and input_list[row_num+2][ch-2] == "A":
                        if len(input_list) > row_num+3 and input_list[row_num+3][ch-3] == "S":
                            print("found XMAS left diagonal")
                            match = match + 1

        if row[ch] == "S":
            # Vertical
            if len(input_list) > row_num+1 and input_list[row_num+1][ch] == "A":
                if len(input_list) > row_num+2 and input_list[row_num+2][ch] == "M":
                    if len(input_list) > row_num+3 and input_list[row_num+3][ch] == "X":
                        print("found SAMX vertical")
                        match = match + 1

            # Diagonal
            if ch < 3: # check only right
                if len(input_list) > row_num+1 and input_list[row_num+1][ch+1] == "A":
                    if len(input_list) > row_num+2 and input_list[row_num+2][ch+2] == "M":
                        if len(input_list) > row_num+3 and input_list[row_num+3][ch+3] == "X":
                            print("found SAMX right diagonal")
                            match = match + 1
            elif ch > 136: # check only left
                if len(input_list) > row_num+1 and input_list[row_num+1][ch-1] == "A":
                    if len(input_list) > row_num+2 and input_list[row_num+2][ch-2] == "M":
                        if len(input_list) > row_num+3 and input_list[row_num+3][ch-3] == "X":
                            print("found SAMX left diagonal")
                            match = match + 1
            else:
                # check right
                if len(input_list) > row_num+1 and input_list[row_num+1][ch+1] == "A":
                    if len(input_list) > row_num+2 and input_list[row_num+2][ch+2] == "M":
                        if len(input_list) > row_num+3 and input_list[row_num+3][ch+3] == "X":
                            print("found SAMX right diagonal")
                            match = match + 1
                # check left
                if len(input_list) > row_num+1 and input_list[row_num+1][ch-1] == "A":
                    if len(input_list) > row_num+2 and input_list[row_num+2][ch-2] == "M":
                        if len(input_list) > row_num+3 and input_list[row_num+3][ch-3] == "X":
                            print("found SAMX left diagonal")
                            match = match + 1

print(match)