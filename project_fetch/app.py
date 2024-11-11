import json
import random
from pathlib import Path, PosixPath
from typing import Dict, List, Tuple, Union

import streamlit as st
from PIL import Image

from project_fetch import DATA_PATH, MODULE_PATH
from project_fetch.tools import add_to_db


def load_local_files(
) -> Tuple[List[PosixPath], Dict[str, Dict[str, Union[str, List[str]]]]]:
    # Get a list of all images from local folder
    image_folder = F"{DATA_PATH}/tagged"
    image_files = list(Path(image_folder).rglob("*.jpg"))

    # Open local config file
    with open(f"{MODULE_PATH}/questions.json", "r") as file:
        question_config = json.load(file)

    return image_files, question_config


# Load local files
image_files, question_config = load_local_files()

# Extract random question
random_question = random.choice(list(question_config.keys()))

# Extract text-friendly formatted question
question_formatted = question_config[random_question]["question_description"]

# Extract valid answers to question
valid_answers = question_config[random_question]["answers"]

# Append a null value for N/A instances]
valid_answers.append('Unsure')

# Get a random image
image_path = random.choice(image_files)

# Display the question as title
st.title(question_formatted)

# Display the image
try:
    image = Image.open(str(image_path))
    st.image(image, use_container_width=True)
except FileNotFoundError:
    st.error("Image not found. Please check the file path.")

# Create side-by-side buttons dynamically
response = None
cols = st.columns(len(valid_answers))  # One column per answer
for idx, answer in enumerate(valid_answers):
    with cols[idx]:
        if st.button(answer, use_container_width=True):
            response = answer

            if response == 'Unsure':
                response = None
            # Log the response to the database
            add_to_db(
                url=str(image_path),
                question=random_question,
                response=response,
            )
