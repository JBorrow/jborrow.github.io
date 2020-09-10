"""
Looks at what happens when you change neighbour number between SPH and the regular
volume-changing method
"""

import matplotlib

matplotlib.use("Agg")
matplotlib.rc("font", **{"family": "sans-serif", "sans-serif": ["PT Sans Caption"]})

import numpy as np

import make_particles as mp


def get_positions():
    """
    Makes the positions.
    """

    x, y = mp.get_cluster(25, 25, 2, 10002, 9)

    x = np.concatenate([x, np.array([75])])
    y = np.concatenate([y, np.array([75])])

    x = abs(x)
    y = abs(y)

    x = x % 100
    y = y % 50

    return x, y


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from change_volume import get_densities as cv
    from sph import get_densities as sph

    positions = get_positions()
    x = np.linspace(0, 100, 256)
    y = np.linspace(0, 100, 256)

    for strategy, name in zip([cv, sph], ["change_volume", "sph"]):
        fig, axes = plt.subplots(1, 2, figsize=(9, 2.5))

        densities = [
            strategy(
                *positions, nx=256, ny=256, x_range=(0, 100), y_range=(0, 100), n=x
            )[0]
            for x in [9, 10]
        ]

        for density, n, ax in zip(densities, [9, 10], axes):
            img = ax.pcolormesh(x, y, density)
            ax.scatter(*positions, s=1, c="white")

            ax.text(5, 40, r"N$_{{\rm neigh}}$ = {}".format(n), color="white")

            ax.set_xlabel("$x$ position")
            ax.set_aspect(aspect="equal", adjustable="box")

        axes[0].set_ylabel("$y$ position")

        axes[0].set_xlim(xmin=0, xmax=100)
        axes[0].set_ylim(ymin=0, ymax=50)
        axes[1].set_xlim(xmin=0, xmax=100)
        axes[1].set_ylim(ymin=0, ymax=50)

        axes[1].get_yaxis().set_visible(False)

        fig.tight_layout()

        fig.savefig("{}_neighbour_number.png".format(name), dpi=72 * 2)
