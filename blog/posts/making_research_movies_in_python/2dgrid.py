import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

# Some global variables to define the whole run
total_number_of_frames = 100
all_data = [
    np.random.rand(512, 512) for x in range(100)
]


def animate(frame):
    """
    Animation function. Takes the current frame number (to select the potion of
    data to plot) and a line object to update.
    """

    # Not strictly neccessary, just so we know we are stealing these from
    # the global scope
    global all_data, image

    # We want up-to and _including_ the frame'th element
    image.set_array(all_data[frame])

    return image


# Now we can do the plotting!
fig, ax = plt.subplots(1, figsize=(1, 1))
# Remove a bunch of stuff to make sure we only 'see' the actual imshow
# Stretch to fit the whole plane
fig.subplots_adjust(0, 0, 1, 1)
# Remove bounding line
ax.axis("off")

# Initialise our plot. Make sure you set vmin and vmax!
image = ax.imshow(all_data[0], vmin=0, vmax=1, cmap="jet")

animation = FuncAnimation(
    # Your Matplotlib Figure object
    fig,
    # The function that does the updating of the Figure
    animate,
    # Frame information (here just frame number)
    np.arange(total_number_of_frames),
    # Extra arguments to the animate function
    fargs=[],
    # Frame-time in ms; i.e. for a given frame-rate x, 1000/x
    interval=1000 / 25
)

# Try to set the DPI to the actual number of pixels you're plotting
animation.save("out_2dgrid_j.mp4", dpi=512)
