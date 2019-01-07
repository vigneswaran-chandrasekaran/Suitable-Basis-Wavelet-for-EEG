import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.optimizers import SGD
#from keras.callbacks import EarlyStopping,TensorBoard
from keras.callbacks import Callback
import keras.backend as K
from numpy import genfromtxt
import numpy,os
from sklearn import preprocessing
from keras.callbacks import EarlyStopping,TensorBoard
#X1= genfromtxt('Db2_features.csv', delimiter=',', skip_header=0, usecols=(([2,3,7,8,12,13,17,18])))
#X2= genfromtxt('Db4_features.csv', delimiter=',', skip_header=0, usecols=(([4,9,14,19])))
X3= genfromtxt('Db5_features.csv', delimiter=',', skip_header=0, usecols=(range(0,20)))
#X4= genfromtxt('Db8_features.csv', delimiter=',', skip_header=0, usecols=(([0,1,5,6,10,11,15,16])))

#X=[[]*n for n in range(500)]
X=X3
#for i in range(0,500):
#    X[i]=list(numpy.concatenate((list(X1[i]),list(X2[i]),list(X3[i]),list(X4[i])), axis=None))

X=numpy.array(X)
X=X[100:300,:]

y1=[0]*100
y2=[1]*100
#y3=[3]*100
#y4=[4]*100
#y5=[4]*100

min_max_scaler = preprocessing.MinMaxScaler()
X = min_max_scaler.fit_transform(X)
Y=numpy.array(y1+y2)

main_avg=[];main_std=[]

for itt in range(20):

    skfold = StratifiedKFold(n_splits=5,shuffle=True)
    cv=[]
    cvstd=[]

    for (train,test) in skfold.split(X,Y):
            
            #X_train, X_valid, Y_train, Y_valid = train_test_split(X[train],Y[train], test_size=0.2, shuffle= True,stratify=Y[train])
            model = Sequential()
            model.add(Dense(25, input_dim=X.shape[1], activation='relu'))
            model.add(Dense(30, activation='relu'))
            model.add(Dense(1, activation='sigmoid'))
            model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
            early_stopping_monitor = [EarlyStopping(monitor='val_loss',patience=50, verbose=1, mode='auto')]
            history=model.fit(X[train],Y[train],epochs=150,verbose=0,shuffle=True)
            scores = model.evaluate(X[test], Y[test], verbose=0)
            cv.append(scores[1])
            cvstd.append(scores[0])

    cv=sum(cv)/float(len(cv))
    cvstd=sum(cvstd)/float(len(cvstd))
    print(cv)
    main_avg.append(cv)
    main_std.append(cvstd)

main_avg=numpy.array(main_avg)
main_std=numpy.array(main_std)

print(numpy.mean(main_avg))
print(numpy.mean(main_std))

