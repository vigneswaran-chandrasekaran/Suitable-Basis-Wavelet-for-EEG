# Daubechies-Family-Selection-for-better-EEG-classification
Finding the best Daubechies Family wavelet which can better approximate the non-stationary EEG signals and effectively classify them for seizure detection.

1)Raw eeg (time domain) signal is obtained from the patient.

2)The signal is decomposed with various Daubechies wavelet family upto 4 levels which give 5 sub band frequencies of orginal signal.

3)In this work db2,db4,db6,db8,db10,db12 are utilized.

4)From the wavelet coeff Sample, Shannon, Renyi (alpha=2) and Permutation entropies are extracted for feature vectors.

5)Create hypothesis for selecting the best suitable wavelet by finding the mother wavelet with least entropy value (cost function).

6)Check with various classifiers and conclude.

7)Classifiers utilized are SVM (Radial Basis Function - Gaussian), Multilayer perceptron, K-Nearest Neighbours and Decision tree.



