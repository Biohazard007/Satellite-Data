
# pip install rasterio
# pip install earthpy

import rasterio as rio
from rasterio import plot
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np  
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
                figsize=(10, 16),
                title="True Color Image").figure


    fig1.savefig("static/Results/RBG.png")

    fig2 = ep.plot_rgb(arr_st,
                rgb=(3, 2, 1),
                stretch=True,
                str_clip=0.2,
                figsize=(10, 16),
                title="False Color Image").figure
    fig2.savefig("static/Results/False_Color.png")

    red = l[2].astype('float64')
    nir = l[3].astype('float64')

    ndvi = np.where(
        (red + nir)==0.,
        0,
        (nir - red)/(nir + red)
    )

    remove_bg = ndvi[(ndvi<0) | (ndvi>0)]
    average_ndvi = np.sum(remove_bg)/remove_bg.size
    average_ndvi = round(average_ndvi, 2)

    def result():
        fig3 = plt.figure()
        plt.ylim([1,3])
        plt.plot([-1, 1], [2, 2], color='black', linewidth=3)
        for i in np.arange(-1,1.1,0.1):
            plt.plot([i, i], [1.98, 2.02], color='black', linewidth=1.5)   
        plt.scatter(average_ndvi, 2, s=200, color='green',alpha=1, zorder=3)
        plt.text(-1, 2.5, 'NDVI Average: %.2f'%average_ndvi, color='blue', fontsize=30, fontfamily="serif")
        plt.text(-1.05, 1.8, '-1', color='#13128f', fontsize=15)
        plt.text(0.9, 1.8, '+1', color='#004610', fontsize=15)
        plt.text(-0.025, 1.8, '0', color='#926829', fontsize=15)
        plt.axis('off')
        plt.savefig("static/Results/result_ndvi.png")
        plt.close()
    result()

    fig4 = plt.figure(figsize=(10,7))
    ax = fig4.add_subplot(1, 2, 1)
    image1 = mpimg.imread("static/Results/result_ndvi.png")
    imgplot = plt.imshow(image1)
    plt.axis('off')
    ax = fig4.add_subplot(1, 2, 2)
    image2 = mpimg.imread("static/reference.jpg")
    imgplot = plt.imshow(image2)
    plt.axis('off')
    plt.savefig("static/Results/result.png")

    ndvi_class_bins = [-1.0, -0.5, 0, 0.000000001, 0.2, 0.4, 0.6, 0.8, 1.0]
    ndvi_landsat_class = np.digitize(ndvi, ndvi_class_bins)

    # Apply the nodata mask to the newly classified NDVI data
    ndvi_landsat_class = np.ma.masked_where(
        np.ma.getmask(ndvi), ndvi_landsat_class
    )
    np.unique(ndvi_landsat_class)

    # Define color map
    nbr_colors = ["#13128f", "#3e3117", "#000000", "#926829", "#eab64f", "#0A8125", "#004610", "#013407"]
    nbr_cmap = ListedColormap(nbr_colors)

    # Define class names
    ndvi_cat_names = [
        "[-1, -0.5] Water Bodies",
        "[-0.5, 0] No Vegetation",
        "[0] Background",
        "[0.01, 0.2] Bare Area",
        "[0.2, 0.4] Low Vegetation",
        "[0.4, 0.6] Moderate Vegetation",
        "[0.6, 0.8] Good Vegetation",
        "[0.8, 1.0] High Vegetation",
    ]

    # Get list of classes
    classes = np.unique(ndvi_landsat_class)
    classes = classes.tolist()
    # The mask returns a value of none in the classes. remove that
    classes = classes[0:8]

    # Plot your data
    fig, ax = plt.subplots(figsize=(12, 12))
    im = ax.imshow(ndvi_landsat_class, cmap=nbr_cmap)
    ep.draw_legend(im_ax=im, classes=classes, titles=ndvi_cat_names)
    # ax.set_title(
    #     "Normalized Difference Vegetation Index (NDVI) Visualization",
    #     fontsize=15,
    # )
    plt.title("NDVI Classification", fontsize = 25)
    ax.set_axis_off()
    # Auto adjust subplot to fit figure size
    plt.tight_layout()
    plt.savefig('static/Results/ndvi.png')
    plt.close()
    return ["static/Results/RBG.png","static/Results/False_Color.png", "static/Results/ndvi.png","static/Results/result.png"]

