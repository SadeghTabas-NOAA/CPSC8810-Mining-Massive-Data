
# ---------------------------------------------------------------------------- #
#                             Hydroinformatics Team                            #
# ---------------------------------------------------------------------------- #


# -------------------------- Filling Missing Values -------------------------- #

# Authors:
# Sadegh Sadeghi Tabas, Nushrat Humaira, Siddish, Pawan, Meghan

# This Code is going to use for filling the missing value data in the streamflow datasets using AI
# Group members:            
            
# In[1] Import Libraries
import numpy as np


# In[2]: Select the Dataset 
files = glob.iglob(os.path.join(os.getcwd(),'../Datasets/2- Selected Stations/North America/', "*.txt"))
for file in files:

# In[3]:        # Rest of the code from below link
                # https://www.hatarilabs.com/ih-en/fill-missing-precipitation-data-with-artificial-intelligence-python-keras-tutorial

# In[]: Save the new dataset
            # Output path : ../Datasets/3- Derived Missing Values/North America/
            # filename + _filled + .txt
            #  

# In[]: Save Summary