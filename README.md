# RBI Notifications RAG System

## Overview
This project implements a Retrieval-Augmented Generation (RAG) system specifically designed to query RBI (Reserve Bank of India) notifications. It leverages the LLaMA index and FastAPI to create a responsive and informative query system. The primary goal is to provide users with specific information contained within RBI notifications through an easy-to-use interface.

## Installation

### Prerequisites
- Python 3.8+
- pip

### Steps
1. Clone the repository:
`git clone <repository-url>`
2. Navigate to the project directory:
`cd <project-directory>`
3. Install the required Python packages:
`pip install -r requirements.txt`

## Usage
To start the FastAPI server and access the web interface: 
'uvicorn fast_api:app --reload'
Navigate to `http://127.0.0.1:8000/` in your web browser to interact with the system.

## Code Explanation
- `main.py`: Initializes the query system, setting up the context, available tools, and the ReActAgent for handling queries.
- `create_index.py`: Handles the creation and loading of the LLaMA index used for querying the RBI notifications dataset.
- `pandas_query_engine.py`: Sets up a PandasQueryEngine for querying the notifications dataset directly using pandas.
- `save_notes.py`: Provides functionality to save text-based notes to a file, allowing users to store information retrieved from the system.
- `fast_api.py`: Contains the FastAPI app setup, including routes for displaying the form and handling queries.
- `form_page.html`: HTML template for the web interface, allowing users to submit queries and view responses.

## Packages Used
- `dotenv`: Loads environment variables from a `.env` file, used here to manage API keys securely.
- `llama_index`: A library for building and interacting with vectorized search indexes, used to create a powerful query engine for RBI notifications.
- `FastAPI`: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- `pandas`: Provides high-performance, easy-to-use data structures, and data analysis tools for Python.
- `Jinja2`: A full-featured template engine for Python, used here for rendering the web interface.

## Outputs 
See all outputs in the `output_images` folder 

## Future Improvements
- Expand the dataset to include more comprehensive RBI notifications.
- Enhance HTML parsing capabilities to extract and utilize more structured data from notifications.
- Evaluate different large language models for potential cost reductions and performance improvements.
- Integrate additional query engine tools to expand the system's capabilities.
- Improve the user interface to include features like question and response history.

## Contact
For any queries or contributions, please email: amankothari917@gmail.com.

