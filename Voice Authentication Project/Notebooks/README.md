# README
This folder contains all of the Python Notebooks. The details below outline the standard of parameters used for model building, the naming convention for the input arrays, and a high-level overview of the purpose for each notebook. The notebooks are best viewed in the order outlined below to precisely follow my thought process.

### BASELINE PARAMETERS:
sr = 12000 </br>
n_mfcc = 32 coefficients </br>
n_fft = 2048 or ~171 ms </br>
hop_length = 512 or ~43 ms 

### SAVED NUMPY ARRAYS & BASE DATAFRAMES
x_mfcc.npy : represents the (32) mfcc features generated, which exists as the standard for this project </br>
y_labels.npy : represents the speaker ID labels extracted, and will not be duplicated for any other variant of train/test data </br>
base_x_train : represents the 64% split of baseline model parameters </br>
base_x_test : represents the 20% split of baseline model parameters </br>
base_x_val : represents the 16% split of baseline model parameters </br>
base_y_train : represents the 64% split of one-hot encoded labels for baseline model </br>
base_y_test : represents the 20% split of one-hot encoded labels for baseline model </br>
base_y_val : represents the 16% split of one-hot encoded labels for baseline model </br>
weights : represents the balanced speaker weights used in all models

### NOTEBOOKS (in order)
1. Preparatory.ipynb : </br>
2. Untitled.ipynb : </br>
3. Explorartory.ipynb : </br>
4. Preanalysis.ipynb : </br>
5. CNN_clean.ipynb : </br>
6. CNN_other.ipynb : </br>

### OTHER NOTEBOOKS FOR FUN
CQCC.ipynb : </br>
TIFF.ipynb : 
