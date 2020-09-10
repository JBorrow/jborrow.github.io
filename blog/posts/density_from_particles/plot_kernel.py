"""
Makes a plot of the cubic spline kernel
"""
import matplotlib

matplotlib.use("Agg")
matplotlib.rc("font", **{"family": "sans-serif", "sans-serif": ["PT Sans Caption"]})

from sph import _kernel


def plot_horizontal(y: float, ax, **kwargs):
    """
    plot a horizontal line
    """

    ax.plot([-1000, 1000], [y, y], **kwargs)

    return


def plot_vertical(x: float, ax, **kwargs):
    """
    Plot a vertical line
    """

    ax.plot([x, x], [-1000, 1000], **kwargs)

    return


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots(1, 1, figsize=(6, 4))

    r_over_h = np.linspace(-3, 3, 1000)
    w_ij = [_kernel(x, 1.0) for x in r_over_h]

    plot_horizontal(0, ax, ls="dotted", lw=1.0, c="k")
    plot_vertical(0, ax, ls="dotted", lw=1.0, c="k")

    plot_vertical(2, ax, ls="dotted", lw=1.0, c="C1")
    plot_vertical(-2, ax, ls="dotted", lw=1.0, c="C1")

    plot_vertical(1, ax, ls="dotted", lw=1.0, c="C2")

    ax.annotate(
        s="",
        xy=(0, 0.25 * _kernel(0, 1.0)),
        xytext=(1.0, 0.25 * _kernel(0, 1.0)),
        arrowprops=dict(arrowstyle="<->", color="C2"),
    )

    ax.text(
        0.5, 0.3 * _kernel(0, 1.0), "FWHM, $h$", ha="center", va="center", color="C2"
    )

    ax.text(
        1.95,
        0.25,
        "Cut-off radius $r=2h$",
        va="center",
        ha="right",
        rotation="vertical",
        color="C1",
    )

    ax.plot(r_over_h, w_ij)

    ax.set_ylabel("Kernel $W_{ij}$")
    ax.set_xlabel("Ratio of interparticle separation to smoothing length, $r_{ij}/h_i$")

    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-0.02, 0.5)

    fig.tight_layout()

    fig.savefig("kernel_plot.png", dpi=72 * 2)
