# AOC_SESSION="53616c7465645f5fc682e328a61c9f135ec6ba5864830e6621e593a61343df80d452ec2b7610045245225067aaf7f0f195d30cd543bbc252c3638e53084fa2b5"

## TEST
file_obj_test = open("Day02/day02_input_test.txt")
file_data_test = file_obj_test.read()
lines_test = file_data_test.splitlines()

## PUZZLE
# aocd 02 2021 > aoc_02_input.txt

# PART 1

file_obj = open("Day02/day02_input.txt")
file_data = file_obj.read()
lines = file_data.splitlines()

horizontal = 0
depth = 0

for line in lines:
    unit = int(line[-1])
    if line.lower().startswith("down"):
        depth += unit
    elif line.lower().startswith("up"):
        depth -= unit
    else:
        horizontal += unit

print("horizontal", horizontal)
print("depth", depth)
print("total", horizontal * depth)
    

print(10 * "-")
# PART 2

horizontal = 0
depth = 0
aim = 0

for line in lines:
    unit = int(line[-1])
    if line.startswith("down"):
        aim += unit
    elif line.startswith("up"):
        aim -= unit
    else:
        horizontal += unit
        depth += unit * aim

print("horizontal", horizontal)
print("depth", depth)
print("aim", aim)
print("total", horizontal * depth)



file_obj.close()
