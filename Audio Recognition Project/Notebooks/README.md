# README
This folder contains all of the Python Notebooks. The details below outline the standard of parameters used for model building and a high-level overview of the purpose for each notebook. The notebooks are best viewed in the order outlined below to precisely follow my thought process.

### BASELINE PARAMETERS:
sr = 12000 </br>
n_mfcc = 32 coefficients </br>
n_fft = 2048 or ~171 ms </br>
hop_length = 512 or ~43 ms 

### NOTEBOOKS
1. Preanalysis.ipynb : Verifies all files are stable </br> 
2. Explorartory.ipynb : Performs MFCC feature extraction </br>
3. Preparatory.ipynb : Performs the train/test split and other tasks </br>
4. CNN_clean.ipynb : Model-building process for CNN for the 'clean' data set </br>
5. CNN_other.ipynb : Model-building process for CNN for the 'other' data set
