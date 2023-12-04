import re

with open("./day04_input.txt") as f:
    cards = f.read().splitlines()
    cards = [card.split(":")[1] for card in cards]


### PART 1


def scratch_card(card):
    wins = 0

    winning_numbers, my_numbers = card.split("|")
    winning_numbers = re.findall("\d+", winning_numbers)
    my_numbers = re.findall("\d+", my_numbers)

    for number in my_numbers:
        if number in winning_numbers:
            wins += 1

    return wins


points = 0

for card in cards:
    if wins := scratch_card(card):
        points += 2 ** (wins - 1)

print("total points", points)  # 17782


## PART 2


dict_cards = {i + 1: [1, scratch_card(card)] for i, card in enumerate(cards)}

for card_number, [nb_cards, wins] in dict_cards.items():
    for i in range(nb_cards):
        for j in range(1, wins + 1):
            dict_cards[card_number + j][0] += 1

total_nb_cards = sum([nb_cards for _, [nb_cards, _] in dict_cards.items()])

print("total number of cards", total_nb_cards)  # 8477787
