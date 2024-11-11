import json

# Load JSON data from a file
def load_json(filename):
    """
    Loads JSON data from a file.
    
    Args:
    filename (str): The path to the JSON file to load.
    
    Returns:
    dict: The loaded JSON data.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Save JSON data to a file
def save_json(filename, data):
    """
    Saves the provided JSON data to a file.
    
    Args:
    filename (str): The path to the JSON file to save the data to.
    data (dict): The data to be saved as JSON.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Add a new question-answer pair to the JSON data
def add_question_answer(filename, question_id, question_description, answers):
    """
    Adds a new question-answer pair to the JSON file.
    
    Args:
    filename (str): The path to the JSON file.
    question_id (str): The question identifier (e.g., Q1, Q2).
    question_description (str): The description of the question.
    answers (list): A list of possible answers for the question.
    """
    data = load_json(filename)
    data[question_id] = {
        "question_description": question_description,
        "answers": answers
    }
    save_json(filename, data)

# Retrieve answers for a given question ID
def get_answers(filename, question_id):
    """
    Retrieves the answers for a given question ID from the JSON file.
    
    Args:
    filename (str): The path to the JSON file.
    question_id (str): The question identifier (e.g., Q1, Q2).
    
    Returns:
    list: A list of answers for the specified question.
    """
    data = load_json(filename)
    question_data = data.get(question_id, {})
    return question_data.get("answers", [])
