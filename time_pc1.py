#INCOMPLETE
import plotly.graph_objects as go

from read_hdf import read_hdf
from get_time import get_time

FOLDERNAME = './data/'
# FILENAME = 'HEPD_DIV_20200717_0850_ORB_08795.h5'
FILENAME = 'HEPD_DIV_20200717_0850_ORB_08795.h5'
GROUP = 'HEPD_DIV'
DATASET = 'block1_values'

data = read_hdf(FOLDERNAME + FILENAME, GROUP, DATASET)
date_time = get_time(data)

PC1 = data[:, 5]

fig = go.Figure(data=go.Scatter(x=range(18), y=PC1[0:18]))
fig.show()


