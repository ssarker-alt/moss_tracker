import streamlit as st #type: ignore 
import cv2 #type: ignore 
import numpy as np #type: ignore 
from PIL import Image #type: ignore 
import io 

st.set_page_config(page_title= "Moss Tracker", layout="centered")
st.title("Moss Growth Tracker")

upload_file = st.file_uploader("Upload a panel photo", type=["jpg", "jpeg", "png"])

if upload_file:
    try:
        image = Image.open(upload_file)
        image = image.convert("RGB")  

        image.thumbnail((800,800))
        st.image(image, caption="Uploaded Panel Image", use_container_width=True)

        img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        hsv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV)

        lower