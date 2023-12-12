def sum_number_of_winning_points(cards):
    cards = [card.split(":")[1] for card in cards]

    own_numbers_lst = [
        list(filter(None, numbers))
        for numbers in [
            numbers.split(" ") for numbers in [card.split("|")[0] for card in cards]
        ]
    ]
    winning_numbers_lst = [
        list(filter(None, numbers))
        for numbers in [
            numbers.split(" ") for numbers in [card.split("|")[1] for card in cards]
        ]
    ]

    total = 0

    for own_numbers, winning_numbers in zip(own_numbers_lst, winning_numbers_lst):
        n_matches = len(set(own_numbers) & set(winning_numbers))
        if n_matches != 0:
            total += 2 ** (n_matches - 1)

    return total


def get_number_of_matches(cards):
    cards = [card.split(":")[1] for card in cards]

    own_numbers_lst = [
        list(filter(None, numbers))
        for numbers in [
            numbers.split(" ") for numbers in [card.split("|")[0] for card in cards]
        ]
    ]
    winning_numbers_lst = [
        list(filter(None, numbers))
        for numbers in [
            numbers.split(" ") for numbers in [card.split("|")[1] for card in cards]
        ]
    ]

    matches = []

    for own_numbers, winning_numbers in zip(own_numbers_lst, winning_numbers_lst):
        matches.append(len(set(own_numbers) & set(winning_numbers)))

    return matches


def sum_total_scratchcards(cards):
    matches = get_number_of_matches(cards)

    num_cards = [1] * len(matches)

    for idx, match in enumerate(matches):
        for k in range(match):
            num_cards[idx + 1 + k] += num_cards[idx]

    return sum(num_cards)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        cards = file.read().splitlines()

    print(sum_number_of_winning_points(cards))

    print(sum_total_scratchcards(cards))
