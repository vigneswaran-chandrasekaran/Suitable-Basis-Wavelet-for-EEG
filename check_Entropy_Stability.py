from numpy import genfromtxt
import numpy

X2= genfromtxt('Db2_features.csv', delimiter=',', skip_header=0, usecols=(range(0,20)))
X4= genfromtxt('Db4_features.csv', delimiter=',', skip_header=0, usecols=(range(0,20)))
X6= genfromtxt('Db6_features.csv', delimiter=',', skip_header=0, usecols=(range(0,20)))
X8= genfromtxt('Db8_features.csv', delimiter=',', skip_header=0, usecols=(range(0,20)))


E2= genfromtxt('Db2_energy.csv', delimiter=',', skip_header=0, usecols=(range(0,5)))
E4= genfromtxt('Db4_energy.csv', delimiter=',', skip_header=0, usecols=(range(0,5)))
E6= genfromtxt('Db6_energy.csv', delimiter=',', skip_header=0, usecols=(range(0,5)))
E8= genfromtxt('Db8_energy.csv', delimiter=',', skip_header=0, usecols=(range(0,5)))

X2=X2.T;X4=X4.T;X6=X6.T;X8=X8.T
E2=E2.T;E4=E4.T;E6=E6.T;E8=E8.T

for i in range(0,20):
    
    d1=numpy.mean(E2[i%5])/numpy.mean(X2[i])
    d2=numpy.mean(E4[i%5])/numpy.mean(X4[i])
    d3=numpy.mean(E6[i%5])/numpy.mean(X6[i])
    d4=numpy.mean(E8[i%5])/numpy.mean(X8[i])
    
    arr=[d1,d2,d3,d4]
    
    #print(arr)

    if max(arr)==d1:
        print("D2")
    if max(arr)==d2:
        print("D4")
    if max(arr)==d3:
        print("D6")
    if max(arr)==d4:
        print("D8")