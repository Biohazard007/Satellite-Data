import glob
import earthpy.spatial as es
import earthpy.plot as ep

import rasterio as rio

import matplotlib.pyplot as plt
import numpy as np

landsat = '/content/*.*'
data = glob.glob(landsat)
data.sort()

l = []

for i in data:
    with rio.open(i, 'r') as f:
        l.append(f.read(1))

arr_st = np.stack(l)

##RGB Processing
ep.plot_rgb(arr_st,
            rgb=(2, 1, 0),
            stretch=True,
            str_clip=0.2,
            figsize=(10, 16))
plt.show()

##NDVI Processing
ndvi = es.normalized_diff(arr_st[3], arr_st[2])

ep.plot_bands(ndvi, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))

plt.show()