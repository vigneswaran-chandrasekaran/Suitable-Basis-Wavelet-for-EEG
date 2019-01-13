from numpy import genfromtxt
import numpy
from sklearn import preprocessing,tree
from sklearn.metrics import classification_report, confusion_matrix , accuracy_score
from sklearn.model_selection import StratifiedKFold

X= genfromtxt('Db12_features.csv', delimiter=',', skip_header=0, )

y1=[1]*100
y2=[2]*100
y3=[2]*100
y4=[2]*100
y5=[2]*100

min_max_scaler = preprocessing.MinMaxScaler()
X = min_max_scaler.fit_transform(X)
Y=numpy.array(y1+y2+y3+y4+y5)
#change above for Y
main_avg=[]

for itt in range(20):
    skfold = StratifiedKFold(n_splits=10,shuffle=True)
    cv=[]
    for (train,test) in skfold.split(X,Y):
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(X[train],Y[train])
        y_pred = clf.predict(X[test])
        scoree=accuracy_score(Y[test], y_pred)
        cv.append(scoree)
        print(confusion_matrix(Y[test],y_pred))  
        print(classification_report(Y[test],y_pred)) 
    cv=numpy.array(cv)
    cv=numpy.mean(cv)
    main_avg.append(cv)
main_avg=numpy.array(main_avg)
print(numpy.mean(main_avg))
