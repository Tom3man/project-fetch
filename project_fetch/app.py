import streamlit as st
from design import BooleanQuestion, MultipleChoiceSection
from PIL import Image
from utils import *

# Set the page title
st.title("Image Viewer with Yes/No Options")

questions = ['What colour is the dog?', 'Is there a person present?']

# Upload the image path
image_path = "/Users/freemant/Repositories/Personal/project-fetch/data/tagged/labrador/images/n02099712_2897.jpg"

# Display the image
try:
    image = Image.open(image_path)
    st.image(image, caption="Your Image", use_column_width=True)
except FileNotFoundError:
    st.error("Image not found. Please check the file path.")

