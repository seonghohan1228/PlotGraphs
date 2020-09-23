import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from read_hdf import read_hdf
from detector import detector
from telescope import telescope
from get_time import get_time
from new_cmap import new_cmap
from average_data import average_data

# Defined for testing purposes 
FOLDERNAME = './data/'
FILENAME = 'MEPD_SCI_20200717_0851_ORB_08795.h5'
GROUP = 'MEPD_SCI'
DATASET = 'block1_values'
NPLOTS = 4

data = read_hdf(FOLDERNAME + FILENAME, GROUP, DATASET)
date_time = get_time(data)
detector_data = detector(data)

# Average
for i in range(NPLOTS):
    detector_data[i] = average_data(detector_data[i])

# Plot
fig, axes = plt.subplots(nrows=NPLOTS, ncols=1, figsize=(8, 6))
gs1 = matplotlib.gridspec.GridSpec(NPLOTS, 1)
gs1.update(wspace=0.025, hspace=0.05)

xmin = matplotlib.dates.date2num(date_time[0])
xmax = matplotlib.dates.date2num(date_time[-1])

for i in range(4):
    axes[i].xaxis.set_visible(False)
    im = axes[i].imshow(np.transpose(detector_data[i]), origin='lower', cmap=new_cmap(), aspect='auto', vmax=13)

plt.subplots_adjust(left=0.05, right=0.9, bottom=0.05, top=0.95, wspace=0.2, hspace=0)
cb_ax = fig.add_axes([0.92, 0.05, 0.02, 0.9])
cbar = fig.colorbar(im, cax=cb_ax)

axes[3].xaxis.set_visible(True)
axes[3].xaxis_date()
plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))

plt.xlabel('UT')
axes[3].xaxis.set_label_coords(-0.5, -0.5)
plt.savefig('detector_plot_3_average_skip.png', dpi=600)
plt.show()
