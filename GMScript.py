# This script will combine a DTM, DSM and Orthophoto into a fused image for a sample area of Northern Ireland
# The purpose of this fused image or 'Green Map' is to display five height bands of vegetation

# Modules to import
import rasterio as rio
"""Processes and handles raster data
Used to open and read imported raster files and carry out operations on them
"""
from rasterio.plot import show
"""Shows raster data as an image
Simply displays rasters in their defined coordinate reference system
"""
import numpy as np
"""Works with the raster data in array form
Used to reclassify pixel values of raster arrays
"""
import xarray as xr
"""Labels the dimensions and coordinates of arrays
Helps to digitize the reclassified arrays
"""

# Data to import
DTM = rio.open('C:\\GIS_Ulster\\Programming\\Assignment\\Assignment\\Data\\DTM.tif')
DSM = rio.open('C:\\GIS_Ulster\\Programming\\Assignment\\Assignment\\Data\\DSM.tif')
Ortho = rio.open('C:\\GIS_Ulster\\Programming\\Assignment\\Assignment\\Data\\Ortho.tif')

# Display DTM image to visualise the area we are working with. Other files cover same area.

show(DTM, cmap='gray')


# Display Coordinate Reference System (CRS) of DTM
def display_crs(crsystem):
    """Function to display CRS of DTM image
    inputs: DTM raster
    outputs: CRS
    """

    return 'Coordinate Reference System of DTM: {}'.format(crsystem)


print(display_crs(DTM.crs))


# Now processing of data begins to produce fused image
# Step one: Combine DTM and DSM by subtraction to create nDSM

DTM_Band1 = DTM.read(1, masked=True)  # Creates a masked array
DSM_Band1 = DSM.read(1, masked=True)
NewDTM = DTM_Band1.astype('f4')  # Converts pixel number integers to floating point
NewDSM = DSM_Band1.astype('f4')
nDSM = (NewDSM - NewDTM)  # nDSM calculation


# Step two: Reclassify nDSM into five vegetation height bands: <0.5, 0.5-2, 2-4, 4-10, >10

data_min_value = np.nanmin(nDSM)  # Calculates minimum pixel value
data_max_value = np.nanmax(nDSM)
print('nDSM minimum pixel value =', data_min_value, ', nDSM maximum pixel value =', data_max_value)

class_bins = [-np.inf, 2, 4, 10, np.inf]  # Reclassifies these pixel values into classes 1, 2, 3, 4 & 5 respectively
reclass_nDSM = xr.apply_ufunc(np.digitize, nDSM, class_bins)  # Digitizes nDSM image to be displayed with new classes


# Step three: Calculate NDVI from Orthophoto Bands 1 and 4

num_bands = Ortho.count
print('Number of bands in Ortho image =', num_bands)  # Displays number of bands in Orthophoto
Ortho_Band1 = Ortho.read(1)  # Separates out band 1 (red band) from Ortho into its own array
Ortho_Band4 = Ortho.read(4)  # Separates out band 4 (NIR band) from Ortho into its own array

redBand = Ortho_Band1.astype('f4')
nirBand = Ortho_Band4.astype('f4')
NDVI = (nirBand - redBand) / (nirBand + redBand)  # NDVI calculation


# Step four: Reclassify NDVI

NDVI[np.where(NDVI <= 0.15)] = 0  # Low NDVI values are separated out to distinguish bare ground from vegetation
NDVI[np.where(NDVI > 0.15)] = 100  # High NDVI values are given a new value of 100 to assist in visualisation


# Step five: Fuse reclassified nDSM and NDVI and display final image

clipped_reclass_nDSM = reclass_nDSM[0:2607, 0:3243]  # Clips reclassed nDSM to same size as NDVI
clipped_reclass_NDVI = NDVI[0:2607, 0:3243]
fused_image = (clipped_reclass_nDSM * clipped_reclass_NDVI)  # Fuses two clipped images together into one final raster

show(fused_image, cmap='Greens')  # Displays heights in green, where white is bare ground and dark green is tallest veg
