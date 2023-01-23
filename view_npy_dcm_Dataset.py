###Author: Sean Pickman
##Allows viewing of data(processed) dcm for CT and MRI in form of numpy arrays (.npy) by saving said files in .png form within folder for viewing.
##   e.g. train data from train_input.npy is (570,256,256), so 570 images with each datapoint having numpy.float64

##Note: 
##   Output folder auto created, but slash denoting directory separator will need changing depending on OS 
##   Input data must be manually set for data variable

import numpy as np
from PIL import Image
import os

data_file_to_load = 'train_output.npy'
output = data_file_to_load.split('.')[0]

data = np.load(f'.\\data(processed)\\{data_file_to_load}')
print(f"Done with reading .npy file...\nNow reading data:\n")
print(f"Shape of input data: {data.shape}")

##each image to be taken from data and saved to a png
for i,image in enumerate(data):
    image= (image*255).astype('uint8')
    
    img = Image.fromarray(image)
    try:
        img.save(f'.\\np_dcm_Dataset\\{output}\\{output}_{i}.png')
    except FileNotFoundError:
        os.mkdir(f"{os.getcwd()}\\np_dcm_Dataset\\{output}")
        print("output dir created\n")
        img.save(f'.\\np_dcm_Dataset\\{output}\\{output}_{i}.png')
    if not(i%10) or (i+1) >= len(data):
        print(f"Finished {i}")
print("Done, exiting.")