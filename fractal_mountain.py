import random

import matplotlib.pyplot as plt

# so basically this is the H value aka the Hurst exponent thing,
# change this to like 0.2 or 0.8 to make the mountains look different!!
# PUT YOUR H VALUE RIGHT HERE
H = 0.8

# ok so these are just our two starting points on the line
xs = [0.0, 1.0]
ys = [0.0, 0.0]


# this function like.. does the recursive midpoint displacement stuff
def displace(x1, y1, x2, y2, variance):
    # so basically if the two points are super close we just stop
    if x2 - x1 < 0.01:
        return

    # finding the midpoint which is literally just the average
    x_mid = (x1 + x2) / 2
    y_mid = (y1 + y2) / 2

    # ok so here we add a random bump using a gaussian distribution
    y_mid += random.gauss(0, 1) * variance

    # saving the new midpoint so we can plot it later
    xs.append(x_mid)
    ys.append(y_mid)

    # this is where the variance gets smaller each time,
    # the (1/2)^H thing controls how spiky the mountains are
    new_variance = variance * (0.5 ** H)

    # now we do the same thing for the left half and right half lol
    displace(x1, y1, x_mid, y_mid, new_variance)
    displace(x_mid, y_mid, x2, y2, new_variance)


# ok let's actually run it with our starting points
displace(0.0, 0.0, 1.0, 0.0, 1.0)

# sorting the points by x so the plot doesn't look like a mess
paired = sorted(zip(xs, ys))
xs = [p[0] for p in paired]
ys = [p[1] for p in paired]

# and now we just plot it!! this is the fun part
plt.plot(xs, ys)
plt.title(f"Fractal Mountain (H = {H})")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
