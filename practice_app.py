import cv2
import numpy as np
from PIL import Image
import pillow_heif
import streamlit as st

#heif support for pillow
pillow_heif.register_heif_opener()

#configure the Streamlit app 
st.set_page_config(page_title="Organism Growth Tracker", layout="centered")

#introduction theme and title 
st.title("🌿 Organism Growth Tracker")
st.markdown("Upload your panel image and watch the magic happen! 🌱")
st.markdown("---")

#sidebar for additional information and tips 
with st.sidebar:
    st.header("📘 About This App")
    st.markdown("""
    This app helps you track and visualize moss or similar growth on concrete panels.  
    Upload a photo, and we'll detect green, brown, and yellow growth based on pixel color.  
    """)
    st.markdown("🌞 Tip: Take photos in natural light for best accuracy!")

#uploading image files including heic formats with others 
st.header("📸 Upload or Take a Photo")
option = st.radio("Choose Image Source:", ["Upload Image", "Take Live Photo"])
image = None

if option == "Upload Image":
    upload_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "heic"])
    if upload_file:
        if upload_file.name.endswith(".heic"):
            img = Image.open(upload_file)
            img = img.convert("RGB")
            image = img
        else:
            image = Image.open(upload_file)
elif option == "Take Live Photo":
    camera_image = st.camera_input("Capture photo")
    if camera_image:
        image = Image.open(camera_image)

# --- Once we have an image ---
if image:
    try:
        image = image.convert("RGB")
        image.thumbnail((800, 800))
        img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Resize
        resized = cv2.resize(img_cv, (800, 800))

        # --- Crop the Panel Area ---
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            largest = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest)
            preview = resized.copy()
            cv2.rectangle(preview, (x, y), (x + w, y + h), (0, 255, 0), 2)
            st.image(preview, caption="Detected Panel Area", channels="BGR", use_container_width=True)
            cropped_panel = resized[y:y + h, x:x + w]
        else:
            cropped_panel = resized
            st.warning("Could not auto-detect panel area. Using full image.")

        # --- Growth Detection ---
        hsv = cv2.cvtColor(cropped_panel, cv2.COLOR_BGR2HSV)

        lower_green = np.array([30, 40, 40])
        upper_green = np.array([90, 255, 255])

        lower_brown = np.array([10, 50, 20])
        upper_brown = np.array([30, 255, 200])

        lower_yellow = np.array([15, 100, 100])
        upper_yellow = np.array([35, 255, 255])

        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        mask_brown = cv2.inRange(hsv, lower_brown, upper_brown)
        mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

        combined_mask = cv2.bitwise_or(mask_green, mask_brown)
        combined_mask = cv2.bitwise_or(combined_mask, mask_yellow)

        moss_pixels = np.sum(combined_mask > 0)
        total_pixels = combined_mask.size
        coverage = (moss_pixels / total_pixels) * 100

        # --- Display Results ---
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Original Image")
            st.image(image, use_container_width=True)
        with col2:
            st.subheader("Detected Growth")
            st.image(combined_mask, use_container_width=True)

        st.markdown("### 📊 Growth Analysis")
        st.metric("Moss-Like Coverage (%)", f"{coverage:.2f}")

    except Exception as e:
        st.error(f"Couldn't process the image: {e}")
            
            
            


