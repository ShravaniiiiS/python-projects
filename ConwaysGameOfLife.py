st_name=input('enter your name')
st_usn=input('enter the usn')
st_sec=input('enter your section')
print('\t\tname:'+st_name)
print('\t\tusn:'+st_usn)
print('\t\tsection:'+st_sec)
print('=====================**********========================')

import time

# Define the grid size
rows = 5
cols = 5


# Create the initial grid (0 = dead, 1 = alive)
grid = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Function to print the grid
def print_grid(grid):
    for row in grid:
        for cell in row:
            print('O' if cell else '.', end=' ')
        print()
    print()

# Count the number of alive neighbors
def count_alive_neighbors(grid, x, y):
    count = 0
    for i in range(x - 1, x + 2):  # from x-1 to x+1
        for j in range(y - 1, y + 2):  # from y-1 to y+1
            if (i == x and j == y) or i < 0 or j < 0 or i >= rows or j >= cols:
                continue
            if grid[i][j] == 1:
                count += 1
    return count

# Generate the next generation of the grid
def next_generation(current_grid):
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            alive_neighbors = count_alive_neighbors(current_grid, i, j)
            if current_grid[i][j] == 1:
                if alive_neighbors in [2, 3]:
                    new_grid[i][j] = 1
            else:
                if alive_neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid

# Run the Game of Life
generations = int(input('enter the generations'))
for gen in range(generations):
    print(f"Generation {gen + 1}:")
    print_grid(grid)
    grid = next_generation(grid)
    time.sleep(1)
