from sklearn.model_selection import StratifiedKFold
from numpy import genfromtxt
import numpy
from sklearn import preprocessing
from sklearn.svm import SVC  
from sklearn.metrics import accuracy_score
from pycm import ConfusionMatrix
        
y1=[1]*100
y2=[2]*100
y3=[2]*100
y4=[3]*100
y5=[3]*100

X= genfromtxt('Db2_Stat_features.csv', delimiter=',', skip_header=0, )
min_max_scaler = preprocessing.MinMaxScaler()
X = min_max_scaler.fit_transform(X)
Y=numpy.array(y1+y2+y3+y4+y5)
#change above for desired label 
main_avg=[]

for itt in range(20):
    skfold = StratifiedKFold(n_splits=10,shuffle=True)
    cv=[]
    for (train,test) in skfold.split(X,Y):
        svclassifier = SVC(kernel='rbf',gamma='auto')  
        svclassifier.fit(X[train], Y[train])  
        y_pred = svclassifier.predict(X[test])
        cv.append(accuracy_score(Y[test], y_pred))
        cm = ConfusionMatrix(actual_vector=Y[test], predict_vector=y_pred) # Create CM From Data
        print(cm)
    cv=numpy.array(cv)
    cv=numpy.mean(cv)
    main_avg.append(cv)
main_avg=numpy.array(main_avg)
print(numpy.mean(main_avg))
