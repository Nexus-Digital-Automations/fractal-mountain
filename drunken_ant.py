# so basically we need random to pick which direction the ant goes
import random

# and matplotlib is how we actually draw the path
import matplotlib.pyplot as plt

# ok so the ant starts at the origin (0, 0)
x, y = 0, 0

# these lists keep track of everywhere the ant has been
xs, ys = [x], [y]

# the four possible moves.. up down left right
moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# now we loop 1000 times and each time the ant picks a random direction
for _ in range(1000):
    dx, dy = random.choice(moves)
    x += dx
    y += dy
    xs.append(x)
    ys.append(y)

# and then we just plot it to see the brownian motion path
plt.plot(xs, ys, linewidth=0.5)
plt.title("Drunken Ant - 2D Brownian Motion (1000 steps)")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.show()
