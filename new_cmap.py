import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Creating new colormap
def new_cmap():
    jet = plt.cm.get_cmap('jet', 256)
    newcolors = jet(np.linspace(0, 1, 256))
    white = np.array([256/256, 256/256, 256/256, 1])
    newcolors[0, :] = white
    new_cmap = matplotlib.colors.ListedColormap(newcolors)

    return new_cmap

