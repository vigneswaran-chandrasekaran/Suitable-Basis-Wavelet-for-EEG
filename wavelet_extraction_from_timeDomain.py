import numpy,pywt,glob,errno
"""path="rep/*.txt"
files=glob.glob(path)
path2="rep/*.TXT"
files2=glob.glob(path2)
files=files+files2
files=sorted(files)
data=[]
for name in files:
	with open(name)as fid:
		temp=fid.readlines()
		data.append([float(k) for k in temp])

X=numpy.array(data)
numpy.savetxt("RAW_TIME_DOMAIN_SIGNAL.csv", X, delimiter=",")"""

#When the file aleardy exists
X= numpy.genfromtxt('RAW_TIME_DOMAIN_SIGNAL.csv', delimiter=',', skip_header=0)

d1=[];d2=[];d3=[];d4=[];a4=[]

for k in range(X.shape[0]):
	a=list(X[k])
	db = pywt.Wavelet('db30')
	cA,cD4,cD3,cD2,cD1 = pywt.wavedec(a,db,level=4)
	d1.append(cD1)
	d2.append(cD2)
	d3.append(cD3)
	d4.append(cD4)
	a4.append(cA)
d1=numpy.array(d1)
d2=numpy.array(d2)
d3=numpy.array(d3)
d4=numpy.array(d4)
a4=numpy.array(a4)

numpy.savetxt("db30D1.csv", d1, delimiter=",")
numpy.savetxt("db30D2.csv", d2, delimiter=",")
numpy.savetxt("db30D3.csv", d3, delimiter=",")
numpy.savetxt("db30D4.csv", d4, delimiter=",")
numpy.savetxt("db30A4.csv", a4, delimiter=",")
