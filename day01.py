def repl_str(line: str) -> str:
    numbers_dict: dict[str, str] = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }
    running = ""

    for l in line:
        running += l
        for num_str, num_int in numbers_dict.items():
            if num_str in running:
                running = running.replace(num_str, num_int)
                break
    return running

def find_first_digit(line: str) -> str:
    for char in line:
        if char.isnumeric():
            return char

def solve(input_text: list[str]) -> int:
    sum: int = 0
    for line in input_text:
        replaced_line = repl_str(line)
        first_num = find_first_digit(replaced_line)
        last_num = find_first_digit(reversed(replaced_line))
        sum += int(first_num + last_num)
    return sum

if __name__ == "__main__":
    with open("day01_e.txt", "r") as f:
        puzzle_input = f.read().splitlines()
    
    print(solve(puzzle_input))