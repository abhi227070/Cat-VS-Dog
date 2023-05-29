import streamlit as st
import numpy as  np
import pandas as pd
import tensorflow as tf
import cv2
from PIL import Image, ImageOps

@st.cache_resource()

def ob():
  interpreter = tf.lite.Interpreter(model_path='quantized_model.tflite')
  

  return interpreter

interpreter=ob()
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

st.title("Car Vs Dog Prediction")


uploaded_files = st.file_uploader("Upload Image",type=["jpeg","jpg","png","txt"])
st.write(uploaded_files)
def prediction(img,interpreter):
  size=(256,256)
  image=ImageOps.fit(img,size,Image.ANTIALIAS)
  image=np.asarray(image)
  img_reshape=image[np.newaxis,...]



  #img_sh=cv2.resize(img,(256,256), interpolation=cv2.INTER_AREA)
  #test_img=img_sh.reshape((1,256,256,3))

  try:
    
    image = np.array(img_reshape, dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    ot=int(output_data[0][0])


    if ot==1:
      return "Dog"

    else:
      return "Cat"
  except:
    return "This is not cat or dog."
  
  
if uploaded_files == None:
  st.write("Please upload Image")
else:
  image=Image.open(uploaded_files)

  st.image(image)

if st.button("Predict"):

  result=''

  result=prediction(image,interpreter)

  st.success(result)