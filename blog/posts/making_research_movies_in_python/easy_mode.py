import numpy as np
import matplotlib.pyplot as plt
import sys

# Grab the frame number from python3 easy_mode.py <x>
frame_number = int(sys.argv[1])

# Some global variables to define the whole run
total_number_of_frames = 100
total_width_of_sine_wave = 2 * np.pi

# How far through are we?
current_factor = frame_number / total_number_of_frames

current_x_data = np.linspace(
    0,
    total_width_of_sine_wave * current_factor,
    frame_number
)
current_y_data = np.sin(current_x_data)

# Now we can do the plotting!
plt.plot(current_x_data, current_y_data)

# Have to set these otherwise we will get one ugly plot!
plt.xlim(0, total_width_of_sine_wave)
plt.ylim(-1.2, 1.2)

plt.xlabel("$x$")
plt.ylabel("$\sin(x)$")

# Make me pretty
plt.tight_layout()
plt.savefig("image_{:03d}.png".format(frame_number))

