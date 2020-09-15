import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from read_hdf import read_hdf
from detector import detector
from get_time import get_time
from new_cmap import new_cmap

# Defined for testing purposes 
FILENAME = 'MEPD_SCI_20200717_0851_ORB_08795.h5'
GROUP = 'MEPD_SCI'
DATASET = 'block1_values'

data = read_hdf(FILENAME, GROUP, DATASET)
date_time = get_time(data)
detector_data = detector(data)

# Plot
fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(8, 6))
gs1 = matplotlib.gridspec.GridSpec(4, 1)
gs1.update(wspace=0.025, hspace=0.05)

xmin, xmax = matplotlib.dates.date2num(date_time[0]), matplotlib.dates.date2num(date_time[-1])
for i in range(4):
    axes[i].xaxis.set_visible(False)
    im = axes[i].imshow(np.transpose(detector_data[i]), extent=[xmin, xmax, 0, 64], origin='lower', cmap=new_cmap(), aspect='auto', vmax=13)

plt.subplots_adjust(left=0.05, right=0.9, bottom=0.05, top=0.95, wspace=0.2, hspace=0)
cb_ax = fig.add_axes([0.92, 0.05, 0.02, 0.9])
cbar = fig.colorbar(im, cax=cb_ax)

axes[3].xaxis.set_visible(True)
axes[3].xaxis_date()
plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))

plt.xlabel('UT')
axes[3].xaxis.set_label_coords(-0.5, -0.5)

plt.show()


