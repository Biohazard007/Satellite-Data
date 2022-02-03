import glob
import earthpy.spatial as es
import earthpy.plot as ep
import rasterio as rio
import matplotlib.pyplot as plt
import numpy as np

landsat = 'C:/Users/Rojesh Thapa/PycharmProjects/pythonProject/Satellite-Data/static/Temp/*.tiff'
data = glob.glob(landsat)
data.sort()

l = []

for i in data:
    with rio.open(i, 'r') as f:
        l.append(f.read(1))

arr_st = np.stack(l)
plt.close('all')
fig1 = ep.plot_rgb(arr_st,
                   rgb=(2, 1, 0),
                   stretch=True,
                   str_clip=0.2,
                   figsize=(4, 8)).figure

fig1.savefig("C:/Users/Rojesh Thapa/PycharmProjects/pythonProject/Satellite-Data/static/Results/RBG.png")

ndvi = es.normalized_diff(arr_st[3], arr_st[2])

fig2 = ep.plot_bands(ndvi,
                     cmap="RdYlGn",
                     cols=1,
                     vmin=-1,
                     vmax=1,
                     figsize=(4, 8)).figure

fig2.savefig("C:/Users/Rojesh Thapa/PycharmProjects/pythonProject/Satellite-Data/static/Results/NDVI.png")

import main.py

main.py.my_func()
execfile('main.py')