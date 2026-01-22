from keras.models import load_model
from PIL import Image
import numpy as np
import cv2

#the following are to do with this interactive notebook code

 
from matplotlib import pyplot as plt # this lets you draw inline pictures in the notebooks
import pylab # this allows you to control figure size 
pylab.rcParams['figure.figsize'] = (10.0, 8.0) # this controls figure size in the notebook



###loading model###
age_model = load_model('age_model_pretrained.h5')
gender_model = load_model('gender_model_pretrained.h5')
emotion_model = load_model('emotion_model_pretrained.h5')

# Labels on Age, Gender and Emotion to be predicted
age_ranges = ['1-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35','36-40','41-50','51-60','61-70','71-80','81-90']
gender_ranges = ['male', 'female']
emotion_ranges= ['positive','negative','neutral']

############################
import io
import streamlit as st
bytes_data=None

img_file_buffer=st.camera_input("Take a picture")
if img_file_buffer is not None:
     
     test_image = Image.open(img_file_buffer)
     st.image(test_image, use_column_width=True)
     st.write(type(test_image))
     image = np.asarray(test_image)
     gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
     face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

     i = 0

     for (x,y,w,h) in faces:
             i = i+1
             cv2.rectangle(image,(x,y),(x+w,y+h),(203,12,255),2)

             img_gray=gray[y:y+h,x:x+w]

             emotion_img = cv2.resize(img_gray, (48, 48), interpolation = cv2.INTER_AREA)
             emotion_image_array = np.array(emotion_img)
             emotion_input = np.expand_dims(emotion_image_array, axis=0)
             output_emotion= emotion_ranges[np.argmax(emotion_model.predict(emotion_input))]
            
             gender_img = cv2.resize(img_gray, (100, 100), interpolation = cv2.INTER_AREA)
             gender_image_array = np.array(gender_img)
             gender_input = np.expand_dims(gender_image_array, axis=0)
             output_gender=gender_ranges[np.argmax(gender_model.predict(gender_input))]

             age_image=cv2.resize(img_gray, (200, 200), interpolation = cv2.INTER_AREA)
             age_input = age_image.reshape(-1, 200, 200, 1)
             output_age = age_ranges[np.argmax(age_model.predict(age_input))]


             output_str = str(i) + ": "+  output_gender + ', '+ output_age + ', '+ output_emotion
             st.write(output_str)
            
             col = (0,255,0)

             cv2.putText(image, str(i),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,col,2)
     st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
if bytes_data is None:
     st.stop()
