import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
 
dir='C:/Users/adam_/Documents/MSDA/Data Foundations/Homeworks/'
pima=pd.read_csv(dir+'pima-indians-diabetes.data.csv')
print(pima.shape) #tell me how many rows, columns the dataframe has
 
#examine whether there are missing values
col_NaN_count=pima.isnull().sum() #column-wise sum of missing values
print(col_NaN_count) #we see we don't have any missing values
col_NaN_count=pima.isnull().sum().sum() #total number of missing values - sum across all columns
print(col_NaN_count)
 
#what if I knew the dataset had missing values?... then fix on ingest
pima_fixedMissingVals=pd.read_csv(dir+'pima-indians-diabetes.data.missingvals.csv',na_values='NaN') #could also replace with something other than 'NaN'
pima_fixedMissingVals
 
#examine our dataframe for impossible/illegitimate values
pima.describe()
plt.figure();pima.hist(color='k',alpha=0.5) #we determine from this that BP and BMI have zero values, which are can't be legitimate
 
pima['BP'].replace(0,np.nan,inplace=True) #replace 0 values in BP column only with NaN; inplace=True changes the values in the dataframe
pima['BMI'].replace(0,np.nan,inplace=True) #replace 0 values in BMI column only with NaN
col_NaN_count=pima.isnull().sum() #column-wise sum of null or NaN values
print(col_NaN_count) #now we see how many observations in each column were illegitmate and now contain NaN
pima.describe() #now see min BP and min BMI != 0

#inputations 
pima
pima['BP'].fillna(pima['BP'].mean())  #now let's impute these illegitimate values (that are now NaN) with the column-wise mean
#note, many built-in imputation methods require NaN as the 'before' value
pima['BMI'].fillna(pima['BMI'].mean()) 

#drop observations
pima=pd.read_csv(dir+'pima-indians-diabetes.data.csv')
pima['BP'].replace(0,np.nan,inplace=True) #replace 0 values in BP column only with NaN; inplace=True changes the values in the dataframe
pima['BMI'].replace(0,np.nan,inplace=True) #replace 0 values in BMI column only with NaN
print(pima.shape)
pima_dropNaN=pima.dropna(inplace=True)
print(pima.shape)
pima_drop2obs=pima.drop(pima.index[[0,1]], inplace=True) #drop rows with index 0 and 1
print(pima.shape)
print(pima.head(n=5))

#removing duplicates
pima_dups=pd.read_csv(dir+'pima-indians-diabetes.data.csv')
print(pima_dups.head(n=5))
print(pima_dups.shape)
pima_dropDUPS=pima_dups.drop_duplicates()
print(pima_dropDUPS.head(n=5))
print(pima_dropDUPS.shape)

#drop features (not observations)
pima_dropDPF=pima.drop(["DPF"], axis=1)
pima_dropDPF.describe()

#global replace !!DANGER!!
pima_NaN_all=pima.replace(0, np.nan)
col_NaN_count=pima_NaN_all.isnull().sum()
print(col_NaN_count) #this was really bad bc we replaced our class=1 value with NaN

#normalization: standardization and scaling
pima.describe()
pima_standardize=(pima-pima.mean())/pima.std() #z score transformation
pima_standardize.describe()
pima_scaled=(pima-pima.min())/(pima.max()-pima.min()) #transforms to frequency-like scaling...values between 0 and 1
pima_scaled.describe()

#when to standardize vs. when to scale
print(pima.skew())
#skewness is less than -1 or greater than 1, distribution is highly skewed
#skewness between -1 and -0.5, distribution is slightly skewed
#lack of skewness, value = 0
print(pima.kurt())
#kurtosis values between -2 and 2 are considered acceptable

df=pd.DataFrame({"A":["cat", "dog", "fish", "gecko"], "B":["car", "bike", "skateboard", "hovercraft"]})
print(df)
df.loc[df.A=="dog", "A"]="snake"
print(df)
df["A"]=df["A"].str.replace("snake", "tarantula")
print(df)
df_RidSpider=df[df.A!="tarantula"]
print(df_RidSpider)

with open("testfile.csv", "wb") as file:
    file.write(b'A,B\n')
    np.savetxt(file, df, fmt="%s", delimiter=',')
file.close()
    

























