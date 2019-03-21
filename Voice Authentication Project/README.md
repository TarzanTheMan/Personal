# README
The following text file describes the purpose of all saved .npy arrays, baseline parameters, weights, and location of data sets.
For subsequent models, the variation will be mentioned.

### DATA
The data for this project can be downloaded from here: http://openslr.org/12 </br>
The speakers data is named speakers.csv </br>
The final paper for this project is named Paper.pdf

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
