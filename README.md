# Project Fetch

## Introduction
This repo contains two versions of an app built using streamlit (documentation here: https://docs.streamlit.io/) to allow for ease in tagging images with different characteristics. The first version of the app outputs data to a CSV file, the second a db file. This will spin up a local server from which the tool will run but this can be integrated with a website or server.

This repo is also poetry enabled to allow for easier package management which will need to be installed (documentation here: https://python-poetry.org/docs/).

****

## Pre-requisites

- Images need to be stored in a project_fetch>data>tagged folder
- Poetry needs to be installed and packages installed

****

## Running the scripts
To run the csv version of the app navigate to the '/project_fetch/' folder in a terminal and run the command:

<pre><code>poetry run streamlit run app_csv.py</code></pre>

To run the db version of the app navigate to the '/project_fetch/' folder in a terminal and run the command:

<pre><code>poetry run streamlit run app_db.py</code></pre>

****
