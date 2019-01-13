from scipy.stats import kurtosis,skew
from numpy import genfromtxt
import numpy
import math

d1= genfromtxt('Data/db12D1.csv', delimiter=',', skip_header=0)
d2= genfromtxt('Data/db12D2.csv', delimiter=',', skip_header=0)
d3= genfromtxt('Data/db12D3.csv', delimiter=',', skip_header=0)
d4= genfromtxt('Data/db12D4.csv', delimiter=',', skip_header=0)
d5= genfromtxt('Data/db12A4.csv', delimiter=',', skip_header=0)

def meann(d1,d2,d3,d4,d5):

    mean1=[];mean2=[];mean3=[];mean4=[];mean5=[]
    for i in range(d1.shape[0]):
        mean1.append(numpy.mean(d1[i]))
    for i in range(d2.shape[0]):
        mean2.append(numpy.mean(d2[i]))
    for i in range(d3.shape[0]):
        mean3.append(numpy.mean(d3[i]))
    for i in range(d4.shape[0]):
        mean4.append(numpy.mean(d4[i]))
    for i in range(d5.shape[0]):
        mean5.append(numpy.mean(d5[i]))

    return(mean1,mean2,mean3,mean4,mean5)

def stdd(d1,d2,d3,d4,d5):

    std1=[];std2=[];std3=[];std4=[];std5=[]
    for i in range(d1.shape[0]):
        std1.append(numpy.std(d1[i]))
    for i in range(d2.shape[0]):
        std2.append(numpy.std(d2[i]))
    for i in range(d3.shape[0]):
        std3.append(numpy.std(d3[i]))
    for i in range(d4.shape[0]):
        std4.append(numpy.std(d4[i]))
    for i in range(d5.shape[0]):
        std5.append(numpy.std(d5[i]))

    return(std1,std2,std3,std4,std5)

def kurtosiss(d1,d2,d3,d4,d5):

    kurtosis1=[];kurtosis2=[];kurtosis3=[];kurtosis4=[];kurtosis5=[]
    for i in range(d1.shape[0]):
        kurtosis1.append(kurtosis(d1[i]))
    for i in range(d2.shape[0]):
        kurtosis2.append(kurtosis(d2[i]))
    for i in range(d3.shape[0]):
        kurtosis3.append(kurtosis(d3[i]))
    for i in range(d4.shape[0]):
        kurtosis4.append(kurtosis(d4[i]))
    for i in range(d5.shape[0]):
        kurtosis5.append(kurtosis(d5[i]))

    return(kurtosis1,kurtosis2,kurtosis3,kurtosis4,kurtosis5)

def skeww(d1,d2,d3,d4,d5):

    skew1=[];skew2=[];skew3=[];skew4=[];skew5=[]
    for i in range(d1.shape[0]):
        skew1.append(skew(d1[i]))
    for i in range(d2.shape[0]):
        skew2.append(skew(d2[i]))
    for i in range(d3.shape[0]):
        skew3.append(skew(d3[i]))
    for i in range(d4.shape[0]):
        skew4.append(skew(d4[i]))
    for i in range(d5.shape[0]):
        skew5.append(skew(d5[i]))

    return(skew1,skew2,skew3,skew4,skew5)

print("Mean extracting")
r1,r2,r3,r4,r5=meann(d1,d2,d3,d4,d5)
print("Standard Deviation extracting")
p1,p2,p3,p4,p5=stdd(d1,d2,d3,d4,d5)
print("kurtosis extracting")
sh1,sh2,sh3,sh4,sh5=kurtosiss(d1,d2,d3,d4,d5)
print("skewness extracting")
sa1,sa2,sa3,sa4,sa5=skeww(d1,d2,d3,d4,d5)

X=[r1,r2,r3,r4,r5,p1,p2,p3,p4,p5,sh1,sh2,sh3,sh4,sh5,sa1,sa2,sa3,sa4,sa5]
X=numpy.array(X)
X=X.T

a = numpy.asarray(X)

print(a.shape)

numpy.savetxt("Db12_Stat_features.csv", a, delimiter=",")