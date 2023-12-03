from dataclasses import dataclass
from typing import TypeAlias

Grid: TypeAlias = list[list[str]]

@dataclass(frozen=True)
class Pos:
    y: int
    x: int

@dataclass
class NumWithStartAndEnd:
    num: int
    start_pos: Pos
    end_pos: Pos

def is_part(input_grid: Grid, num:NumWithStartAndEnd) -> bool:
    y = num.start_pos.y
    x_start = num.start_pos.x
    x_end = num.end_pos.x
    max_y = len(input_grid)-1
    max_x = len(input_grid[0])-1
    
    to_check: list[Pos] = []

    for x in range(x_start-1, min(x_end+2, max_x)):
        if y > 0:
            to_check.append(Pos(y-1, x))
        if y < max_y:
            to_check.append(Pos(y+1, x))
    if x_start > 0:
        to_check.append(Pos(y, x_start-1))
    if x_end < max_x:
        to_check.append(Pos(y, x_end+1))
    
    return any(is_symbol(input_grid[pos.y][pos.x]) for pos in to_check)

def gear_pos(input_grid: Grid, num:NumWithStartAndEnd) -> Pos|None:
    y = num.start_pos.y
    x_start = num.start_pos.x
    x_end = num.end_pos.x
    max_y = len(input_grid)-1
    max_x = len(input_grid[0])-1
    
    to_check: list[Pos] = []

    for x in range(x_start-1, min(x_end+2, max_x)):
        if y > 0:
            to_check.append(Pos(y-1, x))
        if y < max_y:
            to_check.append(Pos(y+1, x))
    if x_start > 0:
        to_check.append(Pos(y, x_start-1))
    if x_end < max_x:
        to_check.append(Pos(y, x_end+1))
    
    for pos in to_check:
        if is_star(input_grid[pos.y][pos.x]):
            return pos
    return None

def is_symbol(char:str) -> bool:
    return not char.isnumeric() and char != "."

def is_star(char: str) -> bool:
    return char == "*"

def gear_ratio(nums: list[int]) -> int:
    return nums[0]*nums[1]

def solve_part1(input_grid:Grid) -> int:
    sum = 0
    found_numbers: list[NumWithStartAndEnd] = []
    for (y, line) in enumerate(input_grid):
        x_start: int = None
        x_end: int = None
        num: str = ""
        for (x, char) in enumerate(line):
            reset = False
            if char.isnumeric():
                if not x_start:
                    x_start = x
                x_end = x
                num += char
                reset = x==len(line)-1
            else:
                reset = x_start
            
            if reset:
                found_numbers.append(NumWithStartAndEnd(int(num), Pos(y, x_start), Pos(y, x_end)))
                x_start = None
                x_end = None
                num = ""
            
    for number in found_numbers:
        if is_part(input_grid, number):
            sum+=number.num
        
    return sum

def solve_part2(input_grid:Grid) -> int:
    sum = 0
    found_numbers: list[NumWithStartAndEnd] = []
    found_gears = {}

    for (y, line) in enumerate(input_grid):
        x_start: int = None
        x_end: int = None
        num: str = ""
        for (x, char) in enumerate(line):
            reset = False
            if char.isnumeric():
                if not x_start:
                    x_start = x
                x_end = x
                num += char
                reset = x==len(line)-1
            else:
                reset = bool(x_start)
            
            if reset:
                found_numbers.append(NumWithStartAndEnd(int(num), Pos(y, x_start), Pos(y, x_end)))
                x_start = None
                x_end = None
                num = ""
            
    for number in found_numbers:
        check = gear_pos(input_grid, number)
        if check:
            if check in found_gears:
                found_gears[check].append(number.num)
            else:
                found_gears[check] = [number.num]

    for nums in found_gears.values():
        if len(nums) == 2:
            sum+=gear_ratio(nums)

    return sum

if __name__ == "__main__":
    with open("m.txt", "r") as f:
        puzzle_input = f.read().splitlines()
        split_input: Grid = [
            [char for char in line]
            for line in puzzle_input
        ]
    
    print(solve_part1(split_input))
    print(solve_part2(split_input))