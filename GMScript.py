# Script will combine a DTM, DSM and Orthophoto into a fused image for a sample area of Northern Ireland
# The purpose of this fused image is to make a 'Green Map' displaying three height bands of vegetation

# Modules to import
import rasterio as rio
from rasterio.plot import show
import numpy as np

# Data to import
DTM = rio.open('C:\GIS_Ulster\Programming\Assignment\Data\DTM.tif')
DSM = rio.open('C:\GIS_Ulster\Programming\Assignment\Data\DSM.tif')
Band1 = rio.open('C:\GIS_Ulster\Programming\Assignment\Data\Band1.tif') # Band 1 of Orthophoto
Band4 = rio.open('C:\GIS_Ulster\Programming\Assignment\Data\Band4.tif') # Band 4 of Orthophoto (NIR band)
Ortho = rio.open ('C:\GIS_Ulster\Programming\Assignment\Data\Ortho.tif')

# Display DTM image to visualise the area we are working with. Other files cover same area.
# show(DTM)
print('Coordinate Reference System:', DTM.crs)


# Now processing of data begins to produce fused image
# Step one: Combine DTM and DSM by subtraction to create nDSM


# Step two: Reclassify nDSM

# Step three: Calculate NDVI from Orthophoto Bands 1 and 4

num_bands = Ortho.count
print('Number of bands in image =', num_bands) # Displays number of bands in Orthophoto
Ortho_Band1 = Ortho.read(1) # Separates out band 1 (red band) from Ortho into its own array
Ortho_Band4 = Ortho.read(4) # Separares out band 4 (NIR band) from Ortho into its own array

redBand = Ortho_Band1.astype('f4')
nirBand = Ortho_Band4.astype('f4')
NDVI = (nirBand-redBand)/(nirBand+redBand) # NDVI calculation
show(NDVI)

# Step four: Reclassify NDVI

# Step five: Fuse nDSM and NDVI

# Step six: Display final fused image
