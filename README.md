# GMScript Setup and Installation Instructions

# 1. Introduction
This script will combine a DTM, DSM and Orthophoto into a fused image for a sample area of Northern Ireland. The purpose of this fused image is to make a 'Green Map' displaying five height bands of vegetation.

# 2. Precursors
   
For the script to work, it's important to have an IDE downloaded, such as Pycharm, and also git and conda installed. Instructions for these are:
	
Pycharm: https://www.jetbrains.com/pycharm/download/#section=windows

Git: https://git-scm.com/downloads

Conda: https://docs.anaconda.com/anaconda/install/ 


# 3. Code Setup

Use Git Bash to clone the repository by typing: 	
	
	git clone https://github.com/ia167/Assignment.git
	
Then use Anaconda Prompt to navigate to the location of the repository you just cloned, e.g.:

	cd c:/Users/name/location/of/repository

Again use Anaconda Prompt to set up the environment using the environment.yml file within the repository. Type:

	conda env create -f environment.yml
	conda activate egm722 

This will provide access to the modules required to run the script.

# 4. Running the Code
Open GMScript.py in Pycharm (or other IDE) and change the data folder path to replicate the folder where the data was just cloned into.
e.g. change the path in inverted commas:
	
	
	DTM = rio.open('C:\\GIS_Ulster\\Programming\\Assignment\\Assignment\\Data\\DTM.tif')
	DSM = rio.open('C:\\GIS_Ulster\\Programming\\Assignment\\Assignment\\Data\\DSM.tif')
	Ortho = rio.open('C:\\GIS_Ulster\\Programming\\Assignment\\Assignment\\Data\\Ortho.tif') 

	
The code is now ready to run.

# 5. Using Different Data
The sample DTM, DSM and Orthophoto data provided is just for one small section of Northern Ireland. Other datasets can be inputted to create Green Maps of different areas. 
No preparation is required for new datasets but in total they have to be less than 100 MB in size so clipping on a GIS platform may be necessary.