def rotate_picture(grid):
    rotated = []
    for col in range(len(grid[0])):
        row = ''
        for r in range(len(grid) - 1, -1, -1):
            row += grid[r][col]
        rotated.append(row)
    return rotated

def print_picture(grid):
    for row in grid:
        print(row)

def main():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
    rotated_grid = rotate_picture(grid)
    print_picture(rotated_grid)

if _name_ == "_main_":
    main()
