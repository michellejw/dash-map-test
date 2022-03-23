"""
Create a geojson polygon file from a shapefile. As an example, we will use BOEM lease blocks and protraction
areas in the Gulf of Mexico.

0. Get shapefile polygon data for Gulf of Mexico lease blocks here: https://www.data.boem.gov/Main/Mapping.aspx. 
   I added these into the repository into a data folder, and added the data folder to my .gitignore file so I'm not 
   tracking them. 
   
1. 
"""

import geopandas as gpd
import pandas as pd


# 1. Load the