"""
Includes functions for the "changing volume" strategty.
"""

import matplotlib

matplotlib.use("Agg")
matplotlib.rc("font", **{"family": "sans-serif", "sans-serif": ["PT Sans Caption"]})

import numpy as np
from scipy.spatial import KDTree

from tqdm import tqdm

from typing import Tuple


def get_kdtree(x: np.ndarray, y: np.ndarray):
    """
    Transform the data and return the tree object
    """
    combined_x_y_arrays = np.dstack([y.ravel(), x.ravel()])[0]

    tree = KDTree(combined_x_y_arrays)

    return tree


def get_density_from_neighbours(x: float, y: float, tree: KDTree, n: int = 10):
    """
    Gets the density around the point x, y for a fixed number of neighbours.
    """

    dist, _ = tree.query([[x, y]], k=n)

    radius = dist.max()

    volume = np.pi * radius * radius

    return n / volume


def get_densities(
    x: np.ndarray,
    y: np.ndarray,
    nx: int,
    ny: int,
    x_range: Tuple = (0, 100),
    y_range: Tuple = (0, 100),
    n: int = 30,
) -> np.ndarray:
    """
    Get the density grid that goes with the particle positions.
    """

    x_values = np.linspace(x_range[0], x_range[1], nx)
    y_values = np.linspace(y_range[0], y_range[1], ny)

    density = np.empty((nx, ny))
    tree = get_kdtree(x, y)

    for x in tqdm(range(nx)):
        for y in range(ny):
            density[x, y] = get_density_from_neighbours(
                x_values[x], y_values[y], tree, n
            )

    return density, tree


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from make_particles import get_positions, draw_circle

    fig, ax = plt.subplots(1, figsize=(7, 6))

    positions = get_positions()

    densities, tree = get_densities(*positions, 512, 512)

    img = ax.imshow(densities, extent=[0, 100, 0, 100], origin="lower")
    ax.scatter(*positions, s=1, c="white")

    # Overplot some circles
    draw_circle(75, 75, np.max(tree.query([75, 75], k=30)[0]), "C1", ax)
    draw_circle(25, 25, np.max(tree.query([25, 25], k=30)[0]), "C2", ax)

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    ax.set_xlabel("$x$ position")
    ax.set_ylabel("$y$ position")

    fig.colorbar(img, label="Density", pad=0)

    fig.tight_layout()

    fig.savefig("fixed_mass_data.png", dpi=72 * 2)
