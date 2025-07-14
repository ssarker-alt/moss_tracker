import streamlit as st  # type: ignore
import cv2  # type: ignore
import numpy as np  # type: ignore
from PIL import Image, ExifTags  # type: ignore


st.set_page_config(page_title="Moss Tracker", layout="centered")
st.title("🌱 Moss Growth Tracker")

upload_file = st.file_uploader("Upload a panel photo", type=["jpg", "jpeg", "png"])

def correct_image_orientation(image: Image.Image):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = dict(image._getexif().items())

        if exif[orientation] == 3:
            image = image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image = image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image = image.rotate(90, expand=True)
    except Exception:
        pass
    return image

if upload_file:
    img = load_image(upload_file)
    img = correct_image_orientation(img)

    # Resize large images
    max_size = (800, 800)
    img.thumbnail(max_size, Image.LANCZOS)

    st.image(img, caption="Uploaded Panel Image", use_container_width=True)

    # Convert to OpenCV format
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV)

    # Combine multiple color ranges (green, brown, yellow)
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

    # Calculate coverage
    moss_pixels = np.sum(combined_mask > 0)
    total_pixels = combined_mask.size
    coverage = (moss_pixels / total_pixels) * 100

    st.metric("Moss-Like Coverage (%)", f"{coverage:.2f}")
    st.image(combined_mask, caption="Moss Mask (Green + Brown + Yellow)", use_container_width=True)












