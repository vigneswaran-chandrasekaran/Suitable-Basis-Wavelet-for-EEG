import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split
from numpy import genfromtxt
import numpy,os
from sklearn import preprocessing
from sklearn.svm import SVC  
from sklearn.metrics import classification_report, confusion_matrix , accuracy_score

X= genfromtxt('Db12_features.csv', delimiter=',', skip_header=0, )
"""
#X1= genfromtxt('Db2_features.csv', delimiter=',', skip_header=0, usecols=(([2,3,7,8,12,13,17,18])))
#X3= genfromtxt('Db4_features.csv', delimiter=',', skip_header=0,usecols=(([4,9,14,19])))
#X4= genfromtxt('Db8_features.csv', delimiter=',', skip_header=0, usecols=(([0,1,5,6,10,11,15,16])))
#X=[[]*n for n in range(500)]
#for i in range(0,500):
#   X[i]=list(numpy.concatenate((list(X1[i]),list(X3[i]),list(X4[i])), axis=None))
"""

X=X[100:500,:]

y1=[1]*100
y2=[2]*100
y3=[3]*100
y4=[4]*100
#y5=[3]*100

min_max_scaler = preprocessing.MinMaxScaler()
X = min_max_scaler.fit_transform(X)
Y=numpy.array(y1+y2+y3+y4)
#change above for Y
main_avg=[]

for itt in range(50):

    skfold = StratifiedKFold(n_splits=10,shuffle=True)
    cv=[]
    for (train,test) in skfold.split(X,Y):

        svclassifier = SVC(kernel='rbf',gamma='auto')  
        svclassifier.fit(X[train], Y[train])  
        y_pred = svclassifier.predict(X[test])
        cv.append(accuracy_score(Y[test], y_pred))
        #print(confusion_matrix(Y[test],y_pred))  
        #print(classification_report(Y[test],y_pred)) 

    cv=numpy.array(cv)
    cv=numpy.mean(cv)
    #print(cv)
    main_avg.append(cv)

main_avg=numpy.array(main_avg)
print(numpy.mean(main_avg))