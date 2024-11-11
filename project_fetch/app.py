import streamlit as st
from PIL import Image

# Set the page title
st.title("Image Viewer with Yes/No Options")

# Upload the image path
image_path = "/Users/freemant/Repositories/Personal/project-fetch/data/tagged/labrador/images/n02099712_2897.jpg"

# Display the image
try:
    image = Image.open(image_path)
    st.image(image, caption="Your Image", use_column_width=True)
except FileNotFoundError:
    st.error("Image not found. Please check the file path.")

# Add Yes/No buttons
if st.button("Yes"):
    st.write("You selected Yes!")
elif st.button("No"):
    st.write("You selected No!")
