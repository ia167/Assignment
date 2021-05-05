# Script will combine a DTM, DSM and Orthophoto into a fused image for a sample area of Northern Ireland
# The purpose of this fused image is to make a 'Green Map' displaying three height bands of vegetation

# Modules to import

import rasterio as rio

# Data to import
DTM = rio.open('C:\GIS_Ulster\Programming\Assignment\Data\DTM.tif')
DSM = rio.open('C:\GIS_Ulster\Programming\Assignment\Data\DSM.tif')
Ortho = rio.open('C:\GIS_Ulster\Programming\Assignment\Data\Ortho.tif')

print('image size (width, height): {} x {}'.format(DTM.width, DTM.height))
