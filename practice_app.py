import cv2
import numpy as np
from PIL import Image
import pillow_heif
import streamlit as st

# Enable HEIC support
pillow_heif.register_heif_opener()

# Streamlit app config
st.set_page_config(page_title="Organism Growth Tracker", layout="centered")
st.title("🌿 Organism Growth Tracker")
st.markdown("Upload your panel image and watch the magic happen! 🌱")
st.markdown("---")

with st.sidebar:
    st.header("📘 About This App")
    st.markdown("""
    Upload a photo, and we'll detect green and brown growth based on pixel color.
    """)
    st.markdown("🌞 Tip: Take photos in natural light for best accuracy!")

# Upload image
st.header("📸 Upload or Take a Photo")
option = st.radio("Choose Image Source:", ["Upload Image", "Take Live Photo"])
image = None

if option == "Upload Image":
    upload_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "heic"])
    if upload_file:
        image = Image.open(upload_file).convert("RGB")
elif option == "Take Live Photo":
    camera_image = st.camera_input("Capture photo")
    if camera_image:
        image = Image.open(camera_image).convert("RGB")

if image:
    try:
        image = image.convert("RGB")
        image.thumbnail((800, 800))
        img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # --- Growth Detection ---
        hsv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV)

        # Color Ranges
        green_lower = np.array([30, 40, 40])
        green_upper = np.array([90, 255, 255])

        brown_lower = np.array([10, 50, 20])
        brown_upper = np.array([30, 255, 200])

        # Masks
        mask_green = cv2.inRange(hsv, green_lower, green_upper)
        mask_brown = cv2.inRange(hsv, brown_lower, brown_upper)

        combined_mask = cv2.bitwise_or(mask_green, mask_brown)

        # Show green/brown pixels in white, rest as original
        growth_highlighted = img_cv.copy()
        growth_highlighted[combined_mask > 0] = [255, 255, 255]

        # Coverage calculation
        moss_pixels = np.sum(combined_mask > 0)
        total_pixels = combined_mask.size
        coverage = (moss_pixels / total_pixels) * 100

        # Display images
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Original Image")
            st.image(image, use_container_width=True)
        with col2:
            st.subheader("Detected Growth")
            st.image(cv2.cvtColor(growth_highlighted, cv2.COLOR_BGR2RGB), use_container_width=True)

        st.markdown("### 📊 Growth Analysis")
        st.metric("Moss-Like Coverage (%)", f"{coverage:.2f}")

    except Exception as e:
        st.error(f"Couldn't process the image: {e}")

            
            


