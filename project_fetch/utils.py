import json
import random
from typing import List, Tuple


def get_random_question(json_file: str) -> Tuple[str, List[str], str]:
    """
    Reads a JSON file, selects a random ID, and returns its associated answers and description.

    Args:
        json_file (str): Path to the JSON file.

    Returns:
        Tuple: A tuple containing the random ID (str), list of answers (List[str]), 
               and description (str) for the selected ID.
    """
    # Open and load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Get a random ID from the keys of the loaded data
    random_id = random.choice(list(data.keys()))

    # Get the answers and description for the selected random ID, defaulting to empty list and string
    selected_data = data.get(random_id, {})
    answers = selected_data.get('answers', [])
    description = selected_data.get('description', '')

    return random_id, answers, description
