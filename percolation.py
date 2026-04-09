# so basically we need random for the probability stuff
import random

# and matplotlib to draw our grids
import matplotlib.pyplot as plt

# this is the grid size.. 10x10 like the assignment says
N = 10

# -----------------------------------------------
# *** PUT YOUR PROBABILITY VALUES RIGHT HERE ***
# we test p = 0.40, p = 0.55, and p = 0.70
# -----------------------------------------------
probs = [0.40, 0.55, 0.70]


# this function checks if there's a path of black squares
# from the top row all the way to the bottom row
def percolates(grid):
    # start with all the black squares in the top row
    visited = set()
    stack = []
    for c in range(N):
        if grid[0][c] == 1:
            stack.append((0, c))
            visited.add((0, c))

    # now we check neighbors (up down left right, no diagonals)
    while stack:
        r, c = stack.pop()
        # if we reached the bottom row then it percolates!!
        if r == N - 1:
            return True
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited and grid[nr][nc] == 1:
                visited.add((nr, nc))
                stack.append((nr, nc))
    return False


# ok now we make a grid for each probability and plot them side by side
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

for i, p in enumerate(probs):
    # filling each square black (1) with probability p, white (0) otherwise
    grid = [[1 if random.random() < p else 0 for _ in range(N)] for _ in range(N)]

    # checking if this grid percolates (connected path top to bottom)
    result = "Yes" if percolates(grid) else "No"

    # drawing the grid.. black squares are filled, white are empty
    axes[i].imshow(grid, cmap="Greys", interpolation="none")
    axes[i].set_title(f"p = {p} (Percolates: {result})")
    axes[i].set_xticks(range(N))
    axes[i].set_yticks(range(N))
    axes[i].grid(True, linewidth=0.5)

plt.suptitle("Percolation Game - 10x10 Grid")
plt.tight_layout()
plt.show()
