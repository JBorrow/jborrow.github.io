import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

# Some global variables to define the whole run
total_number_of_frames = 100
total_width_of_sine_wave = 2 * np.pi
all_x_data = np.linspace(0, total_width_of_sine_wave, total_number_of_frames)
all_y_data = np.sin(all_x_data)


def animate(frame, line):
    """
    Animation function. Takes the current frame number (to select the potion of
    data to plot) and a line object to update.
    """

    # Not strictly neccessary, just so we know we are stealing these from
    # the global scope
    global all_x_data, all_y_data

    # We want up-to and _including_ the frame'th element
    current_x_data = all_x_data[: frame + 1]
    current_y_data = all_y_data[: frame + 1]

    line.set_xdata(current_x_data)
    line.set_ydata(current_y_data)

    # This comma is necessary!
    return (line,)


# Now we can do the plotting!
fig, ax = plt.subplots(1)
# Initialise our line
line, = ax.plot([0], [0])

# Have to set these otherwise we will get one ugly plot!
ax.set_xlim(0, total_width_of_sine_wave)
ax.set_ylim(-1.2, 1.2)

ax.set_xlabel("$x$")
ax.set_ylabel("$\sin(x)$")

# Make me pretty
fig.tight_layout()

animation = FuncAnimation(
    # Your Matplotlib Figure object
    fig,
    # The function that does the updating of the Figure
    animate,
    # Frame information (here just frame number)
    np.arange(total_number_of_frames),
    # Extra arguments to the animate function
    fargs=[line],
    # Frame-time in ms; i.e. for a given frame-rate x, 1000/x
    interval=1000 / 25
)
animation.save("out_funcanimation.mp4")
