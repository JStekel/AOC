def sum_first_and_last_digit_in_lines(lines):
    digits = []

    for line in lines:
        char1 = None
        char2 = None

        for char in line:
            if char.isdigit():
                char1 = char
                break

        for char in line[::-1]:
            if char.isdigit():
                char2 = char
                break

        digits.append(int(char1 + char2))

    return sum(digits)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.read().splitlines()

    print(sum_first_and_last_digit_in_lines(lines))
