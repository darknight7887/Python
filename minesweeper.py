def minesweeper(grid):
    def count_mines_around(i, j):
        # Defines 8 possible directions (horizontally, vertically, and diagonally)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        mine_count = 0
        
        # Checks the grid in each direction to see if a mine is present. If it is,
        # add one to the mine count and then return the total value.
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == "#":
                mine_count += 1

        return str(mine_count)

    # Create a copy of the grid to store the result
    result_grid = [row[:] for row in grid]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "-":
                result_grid[i][j] = count_mines_around(i, j)

    return result_grid

input_grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "#", "#", "#", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "#", "-", "-"]
]

output_grid = minesweeper(input_grid)
for row in output_grid:
    print(" ".join(row))