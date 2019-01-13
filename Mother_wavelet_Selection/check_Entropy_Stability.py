from numpy import genfromtxt
import numpy
X2= genfromtxt('Db2_features.csv', delimiter=',', skip_header=0)
X4= genfromtxt('Db4_features.csv', delimiter=',', skip_header=0)
X6= genfromtxt('Db6_features.csv', delimiter=',', skip_header=0)
X8= genfromtxt('Db8_features.csv', delimiter=',', skip_header=0)
X10= genfromtxt('Db10_features.csv', delimiter=',', skip_header=0)
X12= genfromtxt('Db12_features.csv', delimiter=',', skip_header=0)
E2= genfromtxt('Db2_energy.csv', delimiter=',', skip_header=0, usecols=(range(0,5)))
E4= genfromtxt('Db4_energy.csv', delimiter=',', skip_header=0, usecols=(range(0,5)))
E6= genfromtxt('Db6_energy.csv', delimiter=',', skip_header=0, usecols=(range(0,5)))
E8= genfromtxt('Db8_energy.csv', delimiter=',', skip_header=0, usecols=(range(0,5)))
E10= genfromtxt('Db10_energy.csv', delimiter=',', skip_header=0, usecols=(range(0,5)))
E12= genfromtxt('Db12_energy.csv', delimiter=',', skip_header=0, usecols=(range(0,5)))
X2=X2.T;X4=X4.T;X6=X6.T;X8=X8.T;X10=X10.T;X12=X12.T
E2=E2.T;E4=E4.T;E6=E6.T;E8=E8.T;E10=E10.T;E12=E12.T
arr=[]
for i in range(minn,maxx):
    d1=numpy.mean(X2[i])
    d2=numpy.mean(X4[i])
    d3=numpy.mean(X6[i])
    d4=numpy.mean(X8[i])
    d5=numpy.mean(X10[i])
    d6=numpy.mean(X12[i])
    arr.append([d1,d2,d3,d4,d5,d6])
arr=numpy.array(arr)
print(arr.sum(axis=0))
