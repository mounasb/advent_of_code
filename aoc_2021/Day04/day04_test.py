import re
import numpy as np

with open("Day04/day04_input_test.txt") as f:
    input = f.read().splitlines()

drawn_numbers = input[0]
nb = re.findall('\d+', drawn_numbers)
drawn_numbers = [int(char) for char in nb]
print(drawn_numbers)

print(input[2])
print(input[3])

board = np.empty([5, 5], dtype=int)
board[1]
