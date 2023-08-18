import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from k import res
# Streamlit UI
st.title("Picture Upload and Submit")

# Upload image
uploaded_image = st.file_uploader("Upload a picture", type=["jpg", "png", "jpeg"])

# Display uploaded image
if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Picture", use_column_width=True)

# Load YOLO model and classes


# Submit button
submit_button = st.button("Submit")

# Handle submit action
if submit_button:
    if uploaded_image is not None:
        # Convert uploaded image to numpy array
        image_array = np.array(Image.open(uploaded_image))
        
        # Perform object detection using the res() function
        annotated_image, dic = res(image_array)

        # Display annotated image
        if(len(dic)==0):
            st.image(annotated_image, caption="Objects Not Detected", use_column_width=True)
        else:
            st.image(annotated_image, caption=dic, use_column_width=True)

    else:
        st.warning("Please upload an image before submitting.")