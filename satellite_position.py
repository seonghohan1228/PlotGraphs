import plotly.graph_objects as go
import pandas as pd
import numpy as np
import h5py

with h5py.File('./data/HEPD_DIV_20200717_0850_ORB_08795.h5', 'r') as hdf:
    data = np.array(hdf['/HEPD_DIV/block2_values'])

latitude = data[:, 16]
longitude = data[:, 17]

fig = go.Figure(data=go.Scattergeo(lon = longitude, lat = latitude, mode = 'markers'))

fig.update_geos(projection_type="orthographic", landcolor='white', lataxis_showgrid=True, lonaxis_showgrid=True)
fig.update_layout(title = 'Satellite Position')

fig.show()