calibration_vls = []

file = open('input_file1.txt','r')
file_obj = file.readlines()
for line in file_obj:
  calibration_vls.append(line.strip())

num_list=[]
for item in calibration_vls:
    line_num=""
    for char in item:
        if char.isdigit():
            line_num = line_num+char
    num_list.append(line_num)

last_list=[]
for item in num_list:
    var = item[0] + item[-1]
    var = int(var)
    last_list.append(var)

total = sum(last_list)

print(total)
