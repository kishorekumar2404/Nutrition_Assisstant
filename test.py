# -*- coding: utf-8 -*-
# MLP for Pima Indians Dataset Serialize to JSON and HDF5
import numpy as np
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import os
import cv2

json_file = open('model1.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model1.h5")
print("Loaded model from disk")

label=['burger','chicken briyani','dosa','idly','pizza','pongal','poori','white rice']

def classify(img_file):
    img_name = img_file
    test_image = image.load_img('data/test/burger_4.jpeg', target_size = (128, 128))

    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)
    a=np.round(result[0][0])
    b=np.round(result[0][1])
    c=np.round(result[0][2])
    d=np.round(result[0][3])
    a=np.round(result[0][4])
    b=np.round(result[0][5])
    c=np.round(result[0][6])
    d=np.round(result[0][7])

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    if a == 1:
        prediction = 'burger'
        print(prediction)
    elif b == 1:
        prediction = 'chicken briyani'
        print(prediction)
    elif c == 1:
        prediction = 'dosa'
        print(prediction)
    elif d  == 1:
        prediction = 'idly'
        print(prediction)
    elif e == 1:
        prediction = 'pizza'
        print(prediction)
    elif f == 1:
        prediction = 'pongal'
        print(prediction)
    elif g == 1:
        prediction = 'poori'
        print(prediction)
    elif h  == 1:
        prediction = 'white rice'
        print(prediction)


##test_image = image.img_to_array(test_image)
##test_image = np.expand_dims(test_image, axis = 0)
##result = loaded_model.predict(test_image)
##print(result)
##fresult=np.max(result)
##label2=label[result.argmax()]
###print(label2)








