import numpy as np
 
## Identify features to keep/discard based on filter methods ##
from sklearn.feature_selection import VarianceThreshold
#goal is to remove features with variance < some threshold
#filter method that only considers univariate X (doesn't consider impact on Y)
X=[[0,0,1],[0,1,0],[1,0,0],[0,1,1],[0,1,0],[0,1,1]]
#binary or Boolean variables have a Bernoulli distribution whose variance is p(1-p)
X_new=VarianceThreshold(threshold=(.8)*(1-.8)) #p=0.8
X_new.fit_transform(X) #"fit" part calculates the variance, "transform" part drops features based on the threshold
 
#Univariate feature selection - Filter methods (e.g. entropy, correlation coeff, etc.)
#SelectKBest ... calculate some score (F-statistic, Chi square, regression coeff, etc.) and rank order features based on those scores, and then select K best
#k=all, will give scores for all features and make you pick, or set k a priori
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif
 
iris=load_iris()
X,y=iris.data,iris.target #assign IVs and DVs to X and y
X.shape
list(iris.feature_names) #show labels for IVs
list(iris.target_names) #show labels for DV
X_new=SelectKBest(score_func=f_classif,k=2) #specifying F-statistic as the scoring function and saying we want the top 2 features (2 features w/ highest F-statistics)
fit=X_new.fit(X,y) #calculate the F-statistics for each feature
np.set_printoptions(precision=3) #round to 3 decimal points
print(fit.scores_)
features=fit.transform(X) #this returns subsetted X (X with K best features)
print(features)
 
X_new=SelectKBest(score_func=chi2,k=2) #specifying F-statistic as the scoring function and saying we want the top 2 features (2 features w/ highest F-statistics)
fit=X_new.fit(X,y) #calculate the F-statistics for each feature
np.set_printoptions(precision=3) #round to 3 decimal points
print(fit.scores_)
 
#other filter methods, correlation (X1 and y, X2 and y), entropy, information gain
 
## Tree-based feature selection - wrapper method ##
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
 
model=ExtraTreesClassifier() #run a tree-based estimator
model.fit(X,y) #recall, fit is the function that calculates the scores, or 'estimators' in the context of random forests
print(model.feature_importances_) #print 'scores'; again higher score or estimator value = more important
model=SelectFromModel(model, prefit=True)
X_new=model.transform(X)
X_new.shape
X_new

