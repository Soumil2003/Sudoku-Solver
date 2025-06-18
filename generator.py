import random
from copy import deepcopy
from solver import is_valid

def fill_grid(grid):
    numbers = list(range(1,10))
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid(grid,row,col,num):
                        grid[row][col] = num
                        if fill_grid(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def remove_digits(grid, difficulty='medium'):
    removals={
        'easy': 35,
        'medium': 45,
        'hard':55
    }
    num_to_remove = removals.get(difficulty,45)
    puzzle = deepcopy(grid)
    count = 0
    while count < num_to_remove:
        row,col = random.randint(0,8), random.randint(0,8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            count +=1
    return puzzle

def generate_sudoku(difficulty='medium'):
    grid = [[0 for _ in range(9)] for _ in range(9)]
    fill_grid(grid)
    full_sol = deepcopy(grid)
    puzzle = remove_digits(grid,difficulty)
    return puzzle,full_sol