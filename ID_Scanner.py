import streamlit as st
import cv2
import numpy as np
import pandas as pd
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image
st.title("ID Scanner APP")
uploaded_photo = st.file_uploader("pls upload your image",type=['jpg','PNG','jpeg'])

pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'
def Extract_image(img):
    text = pytesseract.image_to_string(img)
    return text

if uploaded_photo is not None :
    img = Image.open(uploaded_photo)
    #convert image to array
    img_array = np.array(img)
    st.image(img_array,caption='uploaded image....') 

    with st.spinner('Extracing text from your id ...'):
        extraced_text=Extract_image(img_array)
        #st.write(extraced_text)
        st.subheader("Extracted text:")
        text_list= extraced_text.splitlines()
        st.write("Organization name : " + text_list[0]+""+text_list[1])
        st.write("Employee name : " +text_list[8])
        st.write(text_list[3])
        st.write(text_list[4])
        st.write(text_list[5])
        st.write(text_list[6])



