import regex

with open("day01_input.txt") as f:
    lines = f.read().splitlines()

### PART 1

total = 0

for line in lines:
    digits = regex.findall("\d", line)
    # only the first and the last digit
    number = int(digits[0] + digits[-1])
    total += number

print(total)  # 56397

### PART 2

total = 0
digits_letters = {
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
choices = "|".join(k for k in digits_letters)

for line in lines:
    # Sometimes words overlap, like "oneight",
    # regex findall overlapped argument is perfect
    # But with re module, a lookahead is necessary : "(?=(\d|{choices}))"
    digits = regex.findall(f"\d|{choices}", line, overlapped=True)
    number = ""

    # only the first and the last digit
    for i in [0, -1]:
        if digits[i] in digits_letters:
            number += digits_letters[digits[i]]
        else:
            number += digits[i]

    total += int(number)

print(total)  # 55701
