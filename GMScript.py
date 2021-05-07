# Script will combine a DTM, DSM and Orthophoto into a fused image for a sample area of Northern Ireland
# The purpose of this fused image is to make a 'Green Map' displaying three height bands of vegetation

# Modules to import
import rasterio as rio
from rasterio.plot import show

# Data to import
DTM = rio.open('C:\GIS_Ulster\Programming\Assignment\Data\DTM.tif')
DSM = rio.open('C:\GIS_Ulster\Programming\Assignment\Data\DSM.tif')
Band1 = rio.open('C:\GIS_Ulster\Programming\Assignment\Data\Band1.tif')
Band4 = rio.open('C:\GIS_Ulster\Programming\Assignment\Data\Band4.tif')

print('image size (width, height): {} x {}'.format(DTM.width, DTM.height))
show(DTM)
show(DSM)
show(Band1)
show(Band4)

# Step one: Combine DTM and DSM by subtraction to create nDSM


# Step two: Reclassify nDSM

# Step three: Calculate NDVI from Orthophoto Bands 1 and 4

# Step four: Reclassify NDVI

# Step five: Fuse nDSM and NDVI

# Step six: Display final fused image



