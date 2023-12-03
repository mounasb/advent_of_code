import re

with open("./day02_input.txt") as f:
    games = f.read().splitlines()


### PART 1

max_colors = {"red": 12, "green": 13, "blue": 14}
possible_ids_sum = 0

for game in games:
    is_possible = True

    game_id = int(re.search("Game\s(\d+)", game).group(1))
    cube_sets = game.split(":")[1].split(";")
    color_count = {"red": 0, "green": 0, "blue": 0}

    for cube_set in cube_sets:
        cubes = cube_set.split(",")
        for cube in cubes:
            value, color = cube.strip().split(" ")
            if int(value) > max_colors[color]:
                is_possible = False
                break
        if is_possible == False:
            break
    else:
        possible_ids_sum += game_id

print("sum of possible_ids :", possible_ids_sum)  # 2164


### PART 2


def color_count(color, cube_sets):
    count = 0

    for cube_set in cube_sets:
        if color_count := re.findall(f"(\d+)\s{color}", cube_set):
            color_count = int(color_count[0])
            count = color_count if count < color_count else count

    return count


total_powers = 0

for game in games:
    cube_sets = game.split(":")[1].split(";")

    red_count = color_count("red", cube_sets)
    green_count = color_count("green", cube_sets)
    blue_count = color_count("blue", cube_sets)

    total_powers += red_count * green_count * blue_count


print("sum of powers", total_powers)
