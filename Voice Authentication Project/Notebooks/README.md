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

### NOTEBOOKS (voice identification)
1. Preanalysis.ipynb : Verifies all files are stable </br> 
2. Explorartory.ipynb : Performs MFCC feature extraction </br>
3. Preparatory.ipynb : Performs the train/test split and other tasks </br>
4. CNN_clean.ipynb : Model-building process for CNN for the 'clean' data set </br>
5. CNN_other.ipynb : Model-building process for CNN for the 'other' data set

### NOTEBOOKS (voice authentication)
CQCC.ipynb : Explores alternate feature extraction methods </br>
TIFF.ipynb : Saves the specshow distribution plot as a TIFF image </br>
Untitled.ipynb : Locates hidden files that corrupted the code for the images
