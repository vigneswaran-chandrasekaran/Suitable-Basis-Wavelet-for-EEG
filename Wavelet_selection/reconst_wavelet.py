import numpy,pywt
#When the file aleardy exists
X= numpy.genfromtxt('RAW_TIME_DOMAIN_SIGNAL.csv', delimiter=',', skip_header=0)
d1=[];d2=[];d3=[];d4=[];a4=[]
main_mse=[]
for k in range(X.shape[0]):
    a=list(X[k])
    db = pywt.Wavelet('db2')
    coeff = pywt.wavedec(a,db,level=4)
    b=pywt.waverec(coeff, db)
    b=b[0:len(a)]
    mse=0
    for i in range(len(a)):
        mse+=(a[i]-b[i])**2
    main_mse.append((mse**(1/2.00)))
main_mse=numpy.array(main_mse)
print(numpy.mean(main_mse))
