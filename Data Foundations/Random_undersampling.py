from collections import Counter
from sklearn.datasets import make_classification
from imblearn.under_sampling import RandomUnderSampler
import numpy as np

#create sample data
X,y=make_classification(n_classes=2, class_sep=2,\
                        weights=[0.1,0.9], n_informative=3,\
                        n_redundant=1, flip_y=0, n_features=20,\
                        n_clusters_per_class=1, n_samples=1000,\
                        random_state=10)

#apply random undersampling to majority class
rus=RandomUnderSampler(random_state=42)
X_res,y_res=rus.fit_sample(X,y)

#show the class sizes before/after random undersampling
print('Original dataset shape {}'.format(Counter(y)))
print('New dataset shape {}'.format(Counter(y_res)))

#write the arrays to file
np.savetxt('C:/Users/adam_/Documents/MSDA/Data Foundations/Classworks/Sampling/undersampling_X_before.csv',X,delimiter=',',newline='\n')
np.savetxt('C:/Users/adam_/Documents/MSDA/Data Foundations/Classworks/Sampling/undersampling_X_after.csv',X_res,delimiter=',',newline='\n')
np.savetxt('C:/Users/adam_/Documents/MSDA/Data Foundations/Classworks/Sampling/undersampling_y_before.csv',y,delimiter=',',newline='\n')
np.savetxt('C:/Users/adam_/Documents/MSDA/Data Foundations/Classworks/Sampling/undersampling_y_after.csv',y_res,delimiter=',',newline='\n')
