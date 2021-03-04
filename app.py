import streamlit as st
import cv2
import numpy as np

st.title('Image Resizing with OpenCV')

st.subheader('Upload the image')

uploaded_file = st.file_uploader('Choose a image file',)

if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    st.image(opencv_image, channels="BGR")
    #image  = uploaded_file.read()
    
    st.subheader('Define new Width and Height')
    
    
    # width = int(st.number_input('Input a new a Width'))
    # height = int(st.number_input('Input a new a Height'))
    width = st.slider('Width', min_value=None, max_value=2000, 
              value=None, step=10, format=None, key=None)
    height = st.slider('Height', min_value=None, max_value=2000, 
              value=None, step=10, format=None, key=None)

    # resize only if both width and height greater than zero
    if width > 0 and height > 0:
        points = ((width, height))
        
        resized_image = cv2.resize(opencv_image , points, interpolation = cv2.INTER_LINEAR)
        
        st.image(resized_image[:,:,::-1])
    