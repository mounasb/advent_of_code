import re

with open("day01_input.txt") as f:
    lines = f.read().splitlines()

### PART 1

total = 0

for line in lines:
    digits = re.findall("\d", line)
    number = int(digits[0] + digits[-1])
    total += number

print(total)

### PART 2

total = 0
digits_eng = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
choices = "|".join(k for k in digits_eng)

for line in lines:
    digits = re.findall(f"(?=(\d|{choices}))", line)
    number = ""

    for i in [0, -1]:
        if digits[i] in digits_eng:
            number += digits_eng[digits[i]]
        else:
            number += digits[i]

    total += int(number)

print(total)
