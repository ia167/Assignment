# GMScript Setup and Installation Instructions

1. Precursors
   
	For the script to work, it's important to have an IDE downloaded, such as Pycharm, and also git installed. Instructions for these are:

	Pycharm: https://www.jetbrains.com/pycharm/download/#section=windows

	Git: https://git-scm.com/downloads


2. Code Setup

	To download the code, click on GMScript.py and save in an appropriate folder. Also download the 'data' folder to the same location as this holds the three datasets that are used in the code.
	
	Open the code in Pycharm, or other IDE, and change the data folder path to replicate the folder where the data was just saved.
	e.g. change the path in inverted commas:
	
	
	DTM = rio.open('C:\\GIS_Ulster\\Programming\\Assignment\\Assignment\\Data\\DTM.tif')
	DSM = rio.open('C:\\GIS_Ulster\\Programming\\Assignment\\Assignment\\Data\\DSM.tif')
	Ortho = rio.open('C:\\GIS_Ulster\\Programming\\Assignment\\Assignment\\Data\\Ortho.tif') 

	
The code is now ready to run.