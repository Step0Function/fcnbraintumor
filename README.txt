https://www.kaggle.com/datasets/chenghanpu/brain-tumor-mri-and-ct-scan

Source database:
    https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=33948305
    https://wiki.cancerimagingarchive.net/display/Public/CPTAC-GBM
    https://wiki.cancerimagingarchive.net/display/Public/TCGA-GBM

Dicom: contains the source file collected from the three websites above.
data(processed): contains the processed data which are saved as .npy type. you can use the traininput.npy and trainoutput.npy as the input and output of the encoder-decoder structure to train the model. Test and Val input and output can be used as test and validation datasets.

To ask Paul:

Do we want to have a classifier determining cancer/tumor
Or do we want to have image segmentation (more adv, but also more useful for end users to find exactly where tumor/cancer is)
--------------------------------
#All this data is (810x256x256)
#train data from train_input.npy is (570,256,256), with each being numpy.float64
#test data from test_input.npy is (150,256,256), with each being numpy.float64
#val data from val_input.npy is (90,256,256), with each being numpy.float64

This data(processed) AND description from kaggle in below section (see below) have little connection to the "original" dicom (.dcm), which:
* many dicom are either 256x256 or 512x512 in width
* 16,448 dicom exist in sources provided (even source 1 has 4,811 dicom)
-------------------------------
Also, it turns out that the data(processed) that I was correlating has no real data.  This can be seen with my  as seen by the Chinese(simplified) discussion: https://www.kaggle.com/datasets/chenghanpu/brain-tumor-mri-and-ct-scan/discussion/358956?resource=download 

chen feng:
Problems after converting npy to png
Why is there basically no information after output.npy is converted into an image? Is that so?
This is what I converted

chenghan pu:
Yes, I remember this is the data of BW, it seems to be like this after acquisition, the information contained in MRI and CT is also different

chen feng:
The input and output are not MRI and CT data, right?
chen feng:
I am looking for a matching dataset of MRI and CT, do you still have it?
--------------------------------
- Pre-processing strategy: The pre-processing data pipeline includes pairing MRI and CT scans according to a specific time interval between CT and MRI scans of the same patient, MRI image registration to a standard template, MRI-CT image registration, intensity normalization, and extracting 2D slices from 3D volumes. The pipeline can be used to obtain classic 2D MRI-CT images from 3D Dicom format MRI and CT scans, which can be directly used as the training data for the end-to-end synthetic CT deep learning networks.
- Detail:
Pairing MRI and CT scan: If the time interval between MRI and CT scans is too long, the information in MRI and CT images will not
match. Therefore, we pair MRI and CT scans according to a certain time interval between CT and MRI scans of the same patient, which
should not exceed half a year.
- MRI image registration: Considering the differences both in the human brain and space coordinates of radiation images during scanning, the dataset must avoid individual differences and unify the coordinates, which means all the CT and MRI images should be registered to the standard template. The generated images can be more accurate after registration. The template proposed by Montreal Neurosciences Institute is called MNI ICBM 152 non-linear 6th Generation Symmetric Average Brain Stereotaxic Registration Model (MNI 152) (Grabneret al., 2006). Affine registration is first applied to register MRI scans to the MNI152 template.
- Intensity normalization: The registered scans have some extreme values, which introduce errors that would affect the generation accuracy. We normalize the image data and eliminated these extreme values by selecting the pixel values ranked at the top 1% and bottom 1% and replacing the original pixel values of these pixels with the pixel values of 1% and 99%.
Extracting 2D slices from 3D volumes: After carrying out the registration, the 3D MRI and CT scans can be represented as 237×197×189 matrices. To ensure the compatibility between training models and inputs, each 3D image is sliced, and 4500 2D MRI-CT image pairs are selected as the final training data.
-----------------------
CT stands for computerized tomography. In medical imaging, CT scan is one of the most commonly performed scans for diagnostic purposes. 
In simple terms, the CT scan uses a rotating X-ray machine, which is capable of taking images of your body from several different angles. 
Like X-rays, it uses radiation energy, which is absorbed and reflected to different degrees by different structures of the body.
-----------------------
MRI stands for magnetic resonance imaging. It is a form of medical imaging that does not require the use of radiation. 
Instead, it uses a combination of powerful magnetic fields, radio waves, and computerized technology to create a detailed image of your body structures.

MRI works on the principle that your body is largely made up of water. Water consists of hydrogen and oxygen atoms. 
The hydrogen atom, which is made up of a single proton and an electron, reacts to the process applied during an MRI scan.

The MRI machine consists of a tunnel-like closed tube, in which the patient lies during the procedure. 
This tube houses a powerful electromagnet. 
