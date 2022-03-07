
# pip install rasterio
# pip install earthpy

import rasterio as rio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np
import glob
from matplotlib.colors import ListedColormap
import earthpy.plot as ep

def ndvi(files_path):
    l=[]
    for i in files_path:
        with rio.open(i, 'r') as f:
            l.append(f.read(1))
    arr_st = np.stack(l)

    fig1 = ep.plot_rgb(arr_st,
                rgb=(2, 1, 0),
                stretch=True,
                str_clip=0.2,
                figsize=(10, 16)).figure


    fig1.savefig("static/Results/RBG.png")

    fig2 = ep.plot_rgb(arr_st,
                rgb=(3, 2, 1),
                stretch=True,
                str_clip=0.2,
                figsize=(10, 16)).figure
    fig2.savefig("static/Results/False_Color.png")

    red = l[2].astype('float64')
    nir = l[3].astype('float64')

    ndvi = np.where(
        (red + nir)==0.,
        0,
        (nir - red)/(nir + red)
    )


    ndvi_class_bins = [-1.0, -0.5, 0, 0.2, 0.4, 0.6, 0.8, 1.0]
    ndvi_landsat_class = np.digitize(ndvi, ndvi_class_bins)

    # Apply the nodata mask to the newly classified NDVI data
    ndvi_landsat_class = np.ma.masked_where(
        np.ma.getmask(ndvi), ndvi_landsat_class
    )
    np.unique(ndvi_landsat_class)

    # Define color map
    # nbr_colors = ["#13128f", "#96601a", "#670f00", "#38bd09", "#013407"]
    nbr_colors = ["#13128f", "#eab64f", "#926829", "#3e3117", "#38bd09", "#008b3a", "#013407"]
    # nbr_colors = ["#13128f", "#96601a", "#670f00", "#38bd09", "#013407"]
    nbr_cmap = ListedColormap(nbr_colors)

    # Define class names
    ndvi_cat_names = [
        "Water Bodies",
        "No Vegetation",
        "Bare Area",
        "Low Vegetation",
        "Moderate Vegetation",
        "Good Vegetation",
        "High Vegetation",
    ]

    # Get list of classes
    classes = np.unique(ndvi_landsat_class)
    classes = classes.tolist()
    # The mask returns a value of none in the classes. remove that
    classes = classes[0:7]

    # Plot your data
    fig, ax = plt.subplots(figsize=(12, 12))
    im = ax.imshow(ndvi_landsat_class, cmap=nbr_cmap)

    ep.draw_legend(im_ax=im, classes=classes, titles=ndvi_cat_names)
    ax.set_title(
        "Normalized Difference Vegetation Index (NDVI) Classes",
        fontsize=14,
    )
    ax.set_axis_off()

    # Auto adjust subplot to fit figure size
    plt.tight_layout()

    plt.savefig('static/Results/ndvi.png')

    return ["static/Results/RBG.png","static/Results/False_Color.png", "static/Results/ndvi.png"]