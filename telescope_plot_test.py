import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from read_hdf import read_hdf
from detector import detector
from telescope import telescope
from get_time import get_time
from new_cmap import new_cmap

# Defined for testing purposes 
FOLDERNAME = './data/'
FILENAME = 'HEPD_DIV_20200717_0850_ORB_08795.h5'
GROUP = 'HEPD_DIV'
DATASET = 'block1_values'
NPLOTS = 3

data = read_hdf(FOLDERNAME + FILENAME, GROUP, DATASET)
date_time = get_time(data)
telescope_data = telescope(data)
# Plot
fig, axes = plt.subplots(nrows=NPLOTS, ncols=1, figsize=(8, 6))
gs1 = matplotlib.gridspec.GridSpec(NPLOTS, 1)
gs1.update(wspace=0.025, hspace=0.05)

xmin, xmax = matplotlib.dates.date2num(date_time[0]), matplotlib.dates.date2num(date_time[-1])
for i in range(3):
    axes[i].xaxis.set_visible(False)
    im = axes[i].imshow(np.transpose(telescope_data[i][:]), origin='lower', cmap=new_cmap(), aspect='auto', vmax=1.5)

plt.subplots_adjust(left=0.05, right=0.9, bottom=0.05, top=0.95, wspace=0.2, hspace=0)
cb_ax = fig.add_axes([0.92, 0.05, 0.02, 0.9])
cbar = fig.colorbar(im, cax=cb_ax)

axes[2].xaxis.set_visible(True)
axes[2].xaxis_date()
plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%HH:%MM'))

plt.xlabel('UT')
axes[2].xaxis.set_label_coords(-0.5, -0.5)

plt.show()

