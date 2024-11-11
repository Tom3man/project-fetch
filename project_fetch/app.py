import streamlit as st
import logging
import warnings
from datetime import datetime
from typing import Optional
import pandas as pd
import click
from utils import get_random_question
from PIL import Image

log = logging.getLogger(__name__)

@click.command(
    help="""Open the Streamlit Web App to Tag Images"""
)
@click.option("--images-path", type=click.STRING, required=False)
def main(images_path: str = None):

    # Set the page title
    st.title("Image Viewer with Yes/No Options")

    # Display the image
    try:
        image = Image.open(images_path)
        st.image(image, caption="Your Image", use_column_width=True)
    except FileNotFoundError:
        st.error("Image not found. Please check the file path.")

    id, answers, question = get_random_question()
