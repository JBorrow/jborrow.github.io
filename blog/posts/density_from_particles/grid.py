"""
Includes functions for gridding the data
"""

import matplotlib

matplotlib.use("Agg")
matplotlib.rc("font", **{"family": "sans-serif", "sans-serif": ["PT Sans Caption"]})

import numpy as np


def grid_data(x: np.ndarray, y: np.ndarray, n_cells: int = 10):
    """
    Returns a grid (2d histogram) of the data.
    """

    h, xbin, ybin = np.histogram2d(x, y, n_cells, range=([0, 100], [0, 100]))

    return h / (100 / n_cells) ** 2, xbin, ybin


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from make_particles import get_positions

    fig, ax = plt.subplots(1, figsize=(7, 6))

    positions = get_positions()

    density, xbin, ybin = grid_data(*positions)
    img = ax.pcolormesh(xbin, ybin, density.T)
    ax.scatter(*positions, s=2, c="white")

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    ax.set_xlabel("$x$ position")
    ax.set_ylabel("$y$ position")

    fig.colorbar(img, label="Density", pad=0)

    fig.tight_layout()

    fig.savefig("grid_data.png", dpi=72 * 2)
