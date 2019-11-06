### Identification of Suitable Basis Wavelet Function for Epileptic Seizure Detection Using EEG Signals


##### Abstract:
Selection of suitable order of Daubechies (DB) wavelet for the decomposition of Electroencephalogram (EEG) signals to detect epileptic seizures is quite challenging, as experimentation is time-consuming. In existing methods, the selection of basis wavelet function for decomposition of EEG signals is carried out by considering the literature or by trial and error method. There is a very little significant literature which discusses the comparative analysis for the identification of suitable basis wavelet function (mother wavelet). However, the existing methods often fail to provide proper justification for selecting the mother wavelets. Hence, this research work addresses the fore-mentioned setback by identifying the suitable basis wavelet function based on wavelet selection methods for epileptic seizure detection. Further, the entropy-based features are extracted and classified using SVM, DT, ANN, and KNN with five complex cases (University of Bonn, Germany EEG dataset): A-B-C-D-E, AB-CD-E, C-D-E, AB-C-D, and ABCD-E. From the entropy analysis, it is evident that while extracting entropy-based features, tenth order of Daubechies wavelet (DB10) is found to be the most suitable basis wavelet function for the accurate detection of Epileptic Seizures. The performance metrics confirm the suitability of the identified basis wavelet function in terms of sensitivity, specificity and classification accuracy. 

###### Keywords: 
Electroencephalogram (EEG), Discrete wavelet transform (DWT), Daubechies (DB), Basis wavelet function (BWF).

##### Highlights:
Finding the best Daubechies Family wavelet which can better approximate the non-stationary EEG signals and effectively classify them for seizure detection.

1)Raw eeg (time domain) signal is obtained from the patient.

2)The signal is decomposed with various Daubechies wavelet family upto 4 levels (5 sub band frequencies of orginal signal).

3)db2,db4,db6,db8,db10,db12 are utilized for comparision.

4)From the Decomposed Wavelet Coeffecients: Sample, Shannon, Renyi (alpha=2) and Permutation entropies were extracted as feature vectors.

5)Selecting the best suitable wavelet among them by least entropy criterion and Reconstruction Error.

6)Verify the criterion reflected in best performing model using various classifiers.

##### Publication details
This work can be found in the [Springer_link](https://link.springer.com/chapter/10.1007/978-981-15-0029-9_48)
Part of the Advances in Intelligent Systems and Computing book series (AISC, volume 1045)
https://doi.org/10.1007/978-981-15-0029-9_48

###### Cite this paper as:
Anila Glory H., Vigneswaran C., Shankar Sriram V.S. (2020) Identification of Suitable Basis Wavelet Function for Epileptic Seizure Detection Using EEG Signals. In: Luhach A., Kosa J., Poonia R., Gao XZ., Singh D. (eds) First International Conference on Sustainable Technologies for Computational Intelligence. Advances in Intelligent Systems and Computing, vol 1045. Springer, Singapore


