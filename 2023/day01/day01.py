def sum_first_and_last_digit(lines):
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


def sum_first_and_last_digit_strings_included(lines):
    import re

    def coalesce(func, input):
        if func(input) is not None:
            return func(input)
        return input

    word_to_digit = {
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

    result = []

    for line in lines:
        str_digits = re.findall(f"(?=(\d|{'|'.join(word_to_digit.keys())}))", line)
        first_digit = coalesce(word_to_digit.get, str_digits[0])
        last_digit = coalesce(word_to_digit.get, str_digits[-1])
        result.append(int(first_digit + last_digit))

    return sum(result)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.read().splitlines()

    print(sum_first_and_last_digit(lines))

    print(sum_first_and_last_digit_strings_included(lines))
