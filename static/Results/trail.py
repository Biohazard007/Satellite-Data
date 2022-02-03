

import rasterio as rio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

bandB = rio.open('C:/Users/Rojesh Thapa/PycharmProjects/pythonProject/Satellite-Data/static/Temp/2020-01-27-00_00_2020-01-27-23_59_Sentinel-2_L2A_B02_(Raw).tiff')
bandG = rio.open('C:/Users/Rojesh Thapa/PycharmProjects/pythonProject/Satellite-Data/static/Temp/2020-01-27-00_00_2020-01-27-23_59_Sentinel-2_L2A_B03_(Raw).tiff')
bandR = rio.open('C:/Users/Rojesh Thapa/PycharmProjects/pythonProject/Satellite-Data/static/Temp/2020-01-27-00_00_2020-01-27-23_59_Sentinel-2_L2A_B04_(Raw).tiff')
bandNIR = rio.open('C:/Users/Rojesh Thapa/PycharmProjects/pythonProject/Satellite-Data/static/Temp/2020-01-27-00_00_2020-01-27-23_59_Sentinel-2_L2A_B08_(Raw).tiff')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
plot.show(bandR, ax=ax1, cmap='Blues') #red
plot.show(bandNIR, ax=ax2, cmap='Blues') #NIR
fig.tight_layout()

red = bandR.read(1).astype('float64')
nir = bandNIR.read(1).astype('float64')

ndvi = np.where(
    (nir + red)==0.,
    0,
    (nir - red)/(nir + red)
)
ndviImage = rio.open('C:/Users/Rojesh Thapa/PycharmProjects/pythonProject/Satellite-Data/static/Results/ndviImage1.png','w',driver='Gtiff',
                           width = bandR.width, height = bandR.height,
                           count=1,
                           crs=bandR.crs,
                           transform=bandR.transform,
                           dtype='float64'
                           ).figure
ndviImage.write(ndvi,1)
ndviImage.close()
ndviImage.savefig("C:/Users/Rojesh Thapa/PycharmProjects/pythonProject/Satellite-Data/Results/try.png")

ndvi = rio.open('C:/Users/Rojesh Thapa/PycharmProjects/pythonProject/Satellite-Data/static/Results/ndviImage1.tiff')
plot.show(ndvi)