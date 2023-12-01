from aocd import numbers

# AOC_SESSION="53616c7465645f5fc682e328a61c9f135ec6ba5864830e6621e593a61343df80d452ec2b7610045245225067aaf7f0f195d30cd543bbc252c3638e53084fa2b5"

nbs = numbers
# nbs = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

# PART 1
current_number = nbs[0]
increase_counter = 0

for n in nbs[1:]:
    if n > current_number:
        increase_counter += 1
    current_number = n

print(increase_counter)

# PART 2
print(10*"-")

count = sum(nbs[:3])
increase_counter = 0

for i, n in enumerate(nbs[1:]):
    if i == len(nbs) - 2:
        break
    current_count = sum(nbs[i:i+3])
    if current_count > count:
        increase_counter += 1
    count = current_count

print(increase_counter)
