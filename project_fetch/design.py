import streamlit as st

class MultipleChoiceSection:
    def __init__(self, title, questions):
        """
        Initialise a multiple-choice section with a title and a list of questions.

        :param title: Title of the section
        :param questions: A dictionary where keys are questions and values are lists of possible answers
        """
        self.title = title
        self.questions = questions
        self.answers = {}

    def display(self):
        """Display the multiple-choice questions and collect answers."""
        st.subheader(self.title)
        for question, options in self.questions.items():
            self.answers[question] = st.selectbox(question, options)
        return self.answers


class BooleanQuestion:
    def __init__(self, question):
        """
        Initialize a Boolean question.

        :param question: The question to be displayed
        """
        self.question = question
        self.answer = None

    def display(self):
        """Display the Boolean question and collect the answer."""

        # Add Yes/No buttons
        if st.button("Yes"):
            st.write("You selected Yes!")
        elif st.button("No"):
            st.write("You selected No!")

