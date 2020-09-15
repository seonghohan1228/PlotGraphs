import h5py
import matplotlib
import numpy as np


# Read HDF5 file <filename>/<group/dataset>
def read_hdf(filename, group, dataset):
    with h5py.File( filename, 'r') as hdf:
        data = np.array(hdf['/' + group + '/' + dataset])

    return data

