#Discretization
import numpy as np
x = np.array([0.2, 6.4, 3.0, 1.6])
bins = np.array([0.0, 1.0, 2.5, 4.0, 10.0])
x_binned = np.digitize(x, bins)
x_binned
#array([1, 4, 3, 2])

bins=np.array([0.0,60.0,70.0,80.0,90.0,100.0])
score=input('Enter a numeric score:')
grade=np.digitize(score,bins)
print('The grade is:',grade) #This discretizes like we want but doesn't give the category labels we prefer

def compute_grade(score): #This discretizes like we want -- with categorical labels that are more meaningful to the user
    if score>100:
        print('This is not a valid score. Enter a score <= 100.')
    elif score<0:
        print('This is not a valid score. Enter a score >= 0.')
    elif score<60:
        score='F'
    elif score>=60 and score <70:
        score='D'
    elif score>=70 and score<80:
        score='C'
    elif score>=80 and score<90:
        score='B'
    elif score>=90 and score<=100:
        score='A'
    return(score)
score=float(input('Enter a numeric score: '))
grade=compute_grade(score)
print('Grade:',grade)

#Binarization
import numpy as np
from sklearn import preprocessing
X = np.array([[1,-1,2],[1,1,2]])
binarizer = preprocessing.Binarizer(threshold=0.0).fit(X) #change threshold value as desired
binaryX = binarizer.transform(X)
print(binaryX)

#Digitize continuous signal (i.e. discretize time-series signal)
N = 10
ix = np.arange(N)
signal = (np.sin(2*np.pi*ix/float(N/2))*20000+30000)
time=ix
print(time)
print(signal)

