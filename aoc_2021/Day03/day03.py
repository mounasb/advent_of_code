## TEST

file_obj_test = open("aoc_2021_03/aoc_2021_03_test.txt")
file_data_test = file_obj_test.read()
lines_test = file_data_test.splitlines()

# print(lines_test)

# file_obj_test.close()


## PUZZLE
# aocd 03 2021 > aoc_03_input.txt

file_obj = open("aoc_2021_03/aoc_2021_03_input.txt")
file_data = file_obj.read()
lines = file_data.splitlines()

zero_count = 0
one_count = 0
gamma_bin = ''
epsilon_bin = ''

for i in range(len(lines[0])):
    for line in lines:
        bit = line[i]
        if bit == '0':
            zero_count += 1
        else:
            one_count += 1
        
    if zero_count > one_count:
        gamma_bin += '0'
        epsilon_bin += '1'
    else:
        gamma_bin += '1'
        epsilon_bin += '0'

    zero_count = 0
    one_count = 0

gamma = int(gamma_bin, 2)
epsilon = int(epsilon_bin, 2)

print("gamma", gamma_bin, gamma)
print("epsilon", epsilon_bin, epsilon)
print(gamma * epsilon)


print(10 * "-")

zero_count = 0
one_count = 0

for line in lines_test:
    bit = line[0]
    if bit == '0':
        zero_count += 1
    else:
        one_count += 1
    
if one_count >= zero_count: 
    oxygen_list = [line for line in lines_test if line[0] == '1']
else:
    co2_list = [line for line in lines_test if line[0] == '0']

zero_count = 0
one_count = 0

while oxygen_list and len(oxygen_list) > 1:
    for i in range(1, len(oxygen_list)):
        for nb in oxygen_list:
            bit = nb[i]
            if bit == '0':
                zero_count += 1
            else:
                one_count += 1

    if one_count >= zero_count:
        oxygen_list = [nb for nb in oxygen_list if nb[i] == '1']
    else:
        oxygen_list = [nb for nb in oxygen_list if nb[i] == '0']

    zero_count = 0
    one_count = 0

print(oxygen_list)





file_obj.close()
