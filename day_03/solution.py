import itertools
import numpy as np
from collections import deque, defaultdict
from heapq import heappop, heappush

# f = [x for x in open("input.txt").read().splitlines()]

d = 265149
# d = 9
# d = 10
d = 10240
# for line in f:
#     print(line)


x = 1
c = 0
while c < d:
    c += x
    if c >= d:
        break
    c += x
    if c >= d:
        break
    x += 1

horiz = abs((c-d+1) - x // 2 ) + 1
vert = x // 2

print(horiz + vert)

def compute_spiral_sum(square_number):
    if square_number == 1:
        return 1  # Special case for the first square

    # Function to compute sum of neighbors
    def sum_of_neighbors(x, y, grid):
        return sum(grid.get((nx, ny), 0) for nx in range(x-1, x+2) for ny in range(y-1, y+2))

    # Initialize grid with the first square
    grid = {(0, 0): 1}

    # Spiral movement variables
    x, y = 0, 0
    dx, dy = 1, 0
    layer, step = 0, 0
    direction_changes = 0

    # Generate the grid values
    for _ in range(2, square_number + 1):
        # Move to the next square
        if step >= 2 * layer:
            dx, dy = -dy, dx  # Change direction
            direction_changes += 1
            if direction_changes % 2 == 0:
                layer += 1
            step = 0
        x, y = x + dx, y + dy
        step += 1

        # Compute the sum of neighbors and assign it to the current square
        grid[x, y] = sum_of_neighbors(x, y, grid)

        # Check if the current square is the target square
        if _ == square_number:
            return grid[x, y]

    return None


grid = {}


i = 1
def generate_spiral_grid(max_number):
    # Initialize the grid with the center point
    grid = {(0, 0): 1}

    # Spiral movement variables
    x, y = 0, 0
    dx, dy = 0, -1
    step = 0
    change = 0

    for n in range(2, max_number + 1):
        # Move to the next square
        if change == 0:
            dx, dy = -dy, dx  # Change direction
            if dy == 0:
                step += 1  # Increase step every 2nd direction change
            change = step
        x, y = x + dx, y + dy
        change -= 1

        # Assign the current number to the grid
        def sum_of_neighbors(x, y, grid):
            return sum(grid.get((nx, ny), 0) for nx in range(x - 1, x + 2) for ny in range(y - 1, y + 2))
        if sum_of_neighbors(x,y, grid) > d:
            print(sum_of_neighbors(x,y,grid))
        grid[x, y] = sum_of_neighbors(x,y,grid)

    return grid

# Example: Generate a spiral grid for the first 25 numbers
spiral_grid_example = generate_spiral_grid(58)

# Convert the grid to a more visual format for display
def format_spiral_grid(grid):
    # Find grid dimensions
    min_x = min(grid.keys(), key=lambda k: k[0])[0]
    max_x = max(grid.keys(), key=lambda k: k[0])[0]
    min_y = min(grid.keys(), key=lambda k: k[1])[1]
    max_y = max(grid.keys(), key=lambda k: k[1])[1]
    max_num_length = len(str(max(grid.values())))

    # Build a 2D array representation
    rows = []
    for y in range(min_y, max_y + 1):
        row = [str(grid.get((x, y), ' ')).rjust(max_num_length) for x in range(min_x, max_x + 1)]
        rows.append(row)

    # Format the rows for printing
    formatted_grid = '\n'.join([' '.join(row) for row in reversed(rows)])
    return formatted_grid

print(format_spiral_grid(spiral_grid_example))