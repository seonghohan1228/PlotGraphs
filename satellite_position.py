from mpl_toolkits.basemap import Basemap
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import h5py

with h5py.File('MEPD_SCI_20200717_0851_ORB_08795.h5', 'r') as hdf:
    data = np.array(hdf['/MEPD_SCI/block2_values'])

latitude = data[:, 16]
longitude = data[:, 17]

m = Basemap(projection='polar')
m.drawcoastlines()
m.drawmeridians(np.arange(0,360,45))
m.drawparallels(np.arange(-90,90,30))

x, y = m(longitude, latitude)
m.plot(x, y, 'r')

plt.show()
