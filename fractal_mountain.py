# so basically we need random for the gaussian noise stuff
import random

# and matplotlib is what we use to actually draw the graph
import matplotlib.pyplot as plt

# so basically this is the H value aka the Hurst exponent thing,
# change this to like 0.2 or 0.8 to make the mountains look different!!
# lower H = super jagged and spiky, higher H = smooth and rolling
# -----------------------------------------------
# *** PUT YOUR H VALUE RIGHT HERE ***
# try H = 0.8, then H = 0.2, then maybe H = 0.5
# -----------------------------------------------
H = 0.8

# ok so these are our two starting endpoints for the line..
# we start at (0, 0) on the left and (1, 0) on the right
# basically a flat line that we're gonna make into mountains
xs = [0.0, 1.0]
ys = [0.0, 0.0]


# this function like.. does the recursive midpoint displacement stuff
# it takes two points (x1,y1) and (x2,y2) and a variance value
# and keeps splitting the line in half and adding random bumps
def displace(x1, y1, x2, y2, variance):
    # so basically if the two points are super close we just stop
    # this is the base case.. like when do we stop recursing
    if x2 - x1 < 0.01:
        return

    # finding the midpoint which is literally just the average of
    # the x values and the y values separately
    x_mid = (x1 + x2) / 2
    y_mid = (y1 + y2) / 2

    # ok so here we add a random bump to the y midpoint
    # random.gauss(0, 1) gives us a number from a normal distribution
    # centered at 0, and then we multiply by variance to scale it
    y_mid += random.gauss(0, 1) * variance

    # saving the new midpoint to our lists so we can plot it later
    xs.append(x_mid)
    ys.append(y_mid)

    # this is where the variance gets smaller each time we go deeper
    # we multiply by (0.5)^H which is the (1/2)^H scaling factor
    # this controls how spiky vs smooth the mountains end up being
    new_variance = variance * (0.5 ** H)

    # now we recurse!! calling displace on the left half of the segment
    displace(x1, y1, x_mid, y_mid, new_variance)
    # and then on the right half of the segment
    displace(x_mid, y_mid, x2, y2, new_variance)


# ok let's actually run it with our starting points (0,0) and (1,0)
# the last argument 1.0 is the initial variance
displace(0.0, 0.0, 1.0, 0.0, 1.0)

# so the points got added in random order during recursion
# we need to sort them by x value so the line connects properly
paired = sorted(zip(xs, ys))
xs = [p[0] for p in paired]
ys = [p[1] for p in paired]

# and now we just plot it!! this is the fun part
plt.plot(xs, ys)
plt.title(f"Fractal Mountain (H = {H})")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
