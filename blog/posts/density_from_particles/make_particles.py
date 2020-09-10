"""
Makes the particle distribution
"""

import matplotlib

matplotlib.use("Agg")
matplotlib.rc("font", **{"family": "sans-serif", "sans-serif": ["PT Sans Caption"]})

import numpy as np
from typing import Tuple


def get_cluster(x: float, y: float, h: float, seed: int, n: int):
    """
    Get a cluster of n points with smoothing length h around x, y in 2D
    space.
    """

    np.random.seed(seed)
    radii = h * np.random.randn(n)
    theta = 2 * np.pi * np.random.rand(n)

    x_positions = radii * np.cos(theta) + x
    y_positions = radii * np.sin(theta) + y

    return x_positions, y_positions


def get_background(x_range: Tuple, y_range: Tuple, n: int, seed: int):
    """
    Get a uniform random background.
    """

    np.random.seed(seed)

    dx = x_range[1] - x_range[0]
    dy = y_range[1] - y_range[0]

    x_positions = dx * np.random.rand(n * n) + x_range[0]
    y_positions = dy * np.random.rand(n * n) + y_range[0]

    return x_positions, y_positions


def get_positions():
    """
    Get the position arrays that we use.
    """

    x_1, y_1 = get_cluster(75, 75, 20, 1000, 100)
    x_2, y_2 = get_cluster(40, 60, 30, 1001, 100)
    x_3, y_3 = get_cluster(60, 25, 40, 1002, 200)

    x_4, y_4 = get_background((0, 100), (0, 100), 20, 1002)

    x = np.concatenate([x_1, x_2, x_3, x_4])
    y = np.concatenate([y_1, y_2, y_3, y_4])

    # Need to wrap just in case some went off edges

    for array in [x, y]:
        array = abs(array)
        array = array % 100

    return x, y


def draw_circle(x: float, y: float, r: float, c: str, ax):
    """
    Draw a circle of colour c and put it on the plot.
    """

    circle = matplotlib.patches.Circle((x, y), radius=r, color=c, fill=False)

    ax.add_artist(circle)

    return circle


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # Make the plot

    fig, ax = plt.subplots(1, figsize=(6, 6))

    ax.scatter(*get_positions(), s=2)

    draw_circle(75, 75, 20, "C1", ax)
    draw_circle(25, 25, 20, "C2", ax)

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    ax.set_xlabel("$x$ position")
    ax.set_ylabel("$y$ position")

    fig.tight_layout()

    fig.savefig("particles_only.png", dpi=72 * 2)
