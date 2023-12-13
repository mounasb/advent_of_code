import numpy as np
import re

with open("./day06_input.txt") as f:
    lines = f.read().splitlines()


### PART 1


def play_game(time, record):
    holding_times = []
    holding_time = 0

    while time >= 0:
        speed = holding_time
        distance = time * speed

        if distance > record:
            holding_times.append(holding_time)

        holding_time += 1
        time -= 1

    return len(holding_times)


time_values = [int(value) for value in re.findall("\d+", lines[0].split(":")[1])]
record_values = [int(value) for value in re.findall("\d+", lines[1].split(":")[1])]
game_values = [(time, record) for time, record in zip(time_values, record_values)]

wins = []

for time, record in game_values:
    wins.append(play_game(time, record))


# numpy's prod function multiplies all the numbers in a list
prod_wins = np.prod(wins)
print(prod_wins)  # 3316275


### PART 2

time = int("".join(re.findall("\d+", lines[0].split(":")[1])))
record = int("".join(re.findall("\d+", lines[1].split(":")[1])))
print(play_game(time, record))  # 27102791
