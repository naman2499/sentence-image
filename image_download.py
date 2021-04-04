import os 
import pandas as pd
import urllib.request
# from ImageClassifier import CreateDataAndModel
from ImageClassifier import Run
import numpy as np
df = pd.read_csv("data_new.csv",error_bad_lines=False) 

os.chdir('/home/naman/Desktop/image/')

# for url in df['img_url']:
#     klass = url.split('/')[4]
#     print(klass)    
#     try:
#         os.mkdir(klass)
#     except:
#         pass
#     os.chdir(f'/home/naman/Desktop/image/data/{klass}')
#     try:
#         urllib.request.urlretrieve(url, f"{url.split('/')[5]}.jpg")
#     except:
#         print('lite ho gaya',url)
#         pass
#     os.chdir('/home/naman/Desktop/image/data')

# main = CreateDataAndModel(file_path="/home/naman/Desktop/image/data/", model_file_name_to_save="model.hdf5", init_lr=0.0001, epochs=10, batch_size=25)

# # Here "./data/" is the data folder where we have the label folder- "apple" and "banana" (Remember to include a "/" after the folder like "./data/" ). Basically, you have to give the data folder path where you have the label folders, it can also be like "./seg_pred/seg_pred/".   

# main.create() # This will create the data and the model for you.
r = Run(model_file_name="model.hdf5") # The model file in your current directory

def pred(loc='/home/naman/Desktop/image/data/aeroplane/2008_001380.jpg.jpg'):
    pred = r.run(loc)
    print(pred)
    return pred
pred()