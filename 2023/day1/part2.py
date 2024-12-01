calibration_vls = []

file = open('input_file2.txt','r')
file_obj = file.readlines()
for line in file_obj:
  calibration_vls.append(line.strip())

last_list = 0

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

for item in calibration_vls:
	num_pos = ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"]
	if "one" in item:
		one_pos = find_all(item, "one")
		for i in one_pos:
			num_pos[i] = 1

	if "two" in item:
		two_pos = find_all(item, "two")
		for i in two_pos:
			num_pos[i] = 2

	if "three" in item:
		three_pos = find_all(item, "three")
		for i in three_pos:
			num_pos[i] = 3

	if "four" in item:
		four_pos = find_all(item, "four")
		for i in four_pos:
			num_pos[i] = 4

	if "five" in item:
		five_pos = find_all(item, "five")
		for i in five_pos:
			num_pos[i] = 5

	if "six" in item:
		six_pos = find_all(item, "six")
		for i in six_pos:
			num_pos[i] = 6

	if "seven" in item:
		seven_pos = find_all(item, "seven")
		for i in seven_pos:
			num_pos[i] = 7

	if "eight" in item:
		eight_pos = find_all(item, "eight")
		for i in eight_pos:
			num_pos[i] = 8

	if "nine" in item:
		nine_pos = find_all(item, "nine")
		for i in nine_pos:
			num_pos[i] = 9

	count = 0
	for num in item:
		if num.isdigit():
			num_pos[count] = int(num)
		count += 1

	for item in num_pos:
		if type(item) == int:
			first_double = item
			break
	for item in reversed(num_pos):
		if type(item) == int:
			second_double = item
			break

	last_list += int(str(first_double) + str(second_double))

print(last_list)
