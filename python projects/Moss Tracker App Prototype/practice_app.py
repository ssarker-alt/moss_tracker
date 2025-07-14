import streamlit as st # type: ignore
import cv2 # type: ignore
import numpy as np # type: ignore
from PIL import Image # type: ignore
import pillow_heif # type: ignore
import io

st.set_page_config(page_title="Organism Tracker",layout="centered")
st.title("🌱 Organism Growth Tracker")

upload_file = st.file_uploader("Upload a panel photo", type=["jpg", "jpeg", "png"])

# Register HEIF support for Pillow
pillow_heif.register_heif_opener()
def convert_heic_to_png(heic_file):
    img = Image.open(heic_file)
    img = img.convert("RGB")
    return img  # you can also save it as .png if needed


if upload_file:
    try:
        image = Image.open(upload_file)
        image = image.convert("RGB")  

        image.thumbnail((800, 800))
        st.image(image, caption="Uploaded Panel Image", use_container_width=True)

        img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        hsv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV)

        lower_green = np.array([30, 40, 40])
        upper_green = np.array([90, 255, 255]) #we have to think of a way to make the computer smarter then just understanding colors 

        lower_brown = np.array([10, 50, 20])
        upper_brown = np.array([30, 255, 200]) #same thing with the brown

        lower_yellow = np.array([15, 100, 100])
        upper_yellow = np.array([35, 255, 255]) #make sure the yellow is correct 


        #add the masks in one go 
        #cnn training would be better


        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        mask_brown = cv2.inRange(hsv, lower_brown, upper_brown)
        mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # Combine all masks
        combined_mask = cv2.bitwise_or(mask_green, mask_brown)
        combined_mask = cv2.bitwise_or(combined_mask, mask_yellow)

        moss_pixels = np.sum(combined_mask > 0)
        total_pixels = combined_mask.size
        coverage = (moss_pixels / total_pixels) * 100

        st.metric("Moss-Like Coverage (%)", f"{coverage:.2f}")
        st.image(combined_mask, caption="Detected Moss Areas", use_container_width=True)

    except Exception as e:
        st.error(f"Couldn't process the image: {e}")

