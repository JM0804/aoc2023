import re

def solve_part1(input_text: list[list[str]]) -> int:
    sum = 0
    index = 1
    for game in input_text:
        marble_dict = {"red": 0,
                       "green": 0,
                       "blue": 0}
        for draw in game:
            marbles = draw.split(",")
            for marble in marbles:
                color = marble.split()[1]
                number = int(marble.split()[0])
                if marble_dict[color] < number:
                    marble_dict[color] = number
        if marble_dict["red"] <= 12 and marble_dict["green"] <= 13 and marble_dict["blue"] <= 14:
            sum += index
        index+=1
    return sum

def solve_part2(input_text: list[list[str]]) -> int:
    sum = 0
    for game in input_text:
        marble_dict = {"red": 0,
                       "green": 0,
                       "blue": 0}
        for draw in game:
            marbles = draw.split(",")
            for marble in marbles:
                color = marble.split()[1]
                number = int(marble.split()[0])
                if marble_dict[color] < number:
                    marble_dict[color] = number
        sum += (marble_dict["red"] * marble_dict["green"] * marble_dict["blue"])
    return sum            




if __name__ == "__main__":
    with open("day02_m.txt", "r") as f:
        puzzle_input = f.read().splitlines()

    split_input = [re.split(";|:", line)[1:] for line in puzzle_input]
    
    print(solve_part1(split_input))
    print(solve_part2(split_input))