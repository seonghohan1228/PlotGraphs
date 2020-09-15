import h5py
import numpy as np
import matplotlib.pyplot as plt

with h5py.File('MEPD_SCI_20200717_0851_ORB_08795.h5', 'r') as hdf:
    data = np.array(hdf['/MEPD_SCI/block2_values'])

TAM = data[:, 0:8]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)
label = ["Bx", "By", "Bz", "", "IGRF Bx", "IGRF By", "IGRF Bz", ""]

for i in range(8):
    if i < 3:
        ax.plot(TAM[:, i], label=label[i])
    if 3 < i < 7:
        ax.plot(TAM[:, i], label=label[i], linestyle='--')

T = []
for i in range(len(TAM)):
    T.append(np.sqrt((TAM[i, 4])**2 + (TAM[i, 5])**2 + (TAM[i, 6])**2))
ax.plot(T, label="IGRF |B|", linestyle='--')

plt.ylim(-60000, 60000)
ax.set_ylabel("Magnetic Field (nT)")
ax.tick_params(direction="in")
plt.legend(loc='upper center', ncol=len(TAM))
plt.show()


