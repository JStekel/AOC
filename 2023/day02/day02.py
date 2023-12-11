import re


def sum_number_of_valid_games(lines):
    games = [line.split(":")[1].split(";") for line in lines]

    games_lst = []

    for idx, game in enumerate(games):
        for grab in game:
            for color in grab.split(","):
                red = re.compile("(?P<red>.+) red").search(color)
                blue = re.compile("(?P<blue>.+) blue").search(color)
                green = re.compile("(?P<green>.+) green").search(color)

                if red:
                    if int(red.groups("red")[0].replace(" ", "")) > 12:
                        games_lst.append(idx + 1)
                if blue:
                    if int(blue.groups("blue")[0].replace(" ", "")) > 14:
                        games_lst.append(idx + 1)
                if green:
                    if int(green.groups("green")[0].replace(" ", "")) > 13:
                        games_lst.append(idx + 1)

    games_lst = list(dict.fromkeys(games_lst))
    return sum(set(range(len(games))) - set(games_lst))


def sum_of_power_of_minimum_set_cubes(lines):
    games = [line.split(":")[1].split(";") for line in lines]

    cubes = []
    for game in games:
        max_red, max_blue, max_green = 0, 0, 0
        for grab in game:
            for color in grab.split(","):
                red = re.compile("(?P<red>.+) red").search(color)
                blue = re.compile("(?P<blue>.+) blue").search(color)
                green = re.compile("(?P<green>.+) green").search(color)

                if red:
                    num_red = int(red.groups("red")[0])
                    if num_red > max_red:
                        max_red = num_red

                if blue:
                    num_blue = int(blue.groups("blue")[0])
                    if num_blue > max_blue:
                        max_blue = num_blue

                if green:
                    num_green = int(green.groups("green")[0])
                    if num_green > max_green:
                        max_green = num_green

        cubes.append(max_red * max_blue * max_green)

    return sum(cubes)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.read().splitlines()

    print(sum_number_of_valid_games(lines))
    print(sum_of_power_of_minimum_set_cubes(lines))
