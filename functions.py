import os
import json
from openai import OpenAI
from pydantic import BaseModel, Field
from IPython.display import HTML, display
import pandas as pd

def responses_call(client, model, system_prompt, criteria_background, criteria_prompt, document): 
    """
    Calls the language model with the provided document and prompts to generate a response.
    """ 
    response = client.responses.create(
    model=model,
    temperature=0,
    instructions=system_prompt,
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": f" Criteria details: {criteria_background}\nCriteria question: {criteria_prompt}"
                },
                {
                    "type": "input_text",
                    "text": f"\nStudy text:\n{document}"
                }
            ]
        },
    ]
)
    response_text = response.output_text
    return response_text   

def extract_responses(client, plain_text_files, folder, model, system_prompt, criteria_background, criteria_prompt):
    """
    Extracts responses from plain text files in the specified folder using the provided prompts.
    """
    responses = []
    for i, file_name in enumerate(plain_text_files):
        with open(os.path.join(folder, file_name), "r", encoding="utf-8") as f:
            document = f.read()
        response_text = responses_call(client,model, system_prompt, criteria_background, criteria_prompt, document)
        resp_dict = {
            'file_name':  file_name,
            'response_text': response_text
        }
        responses.append(resp_dict)
    return responses

def add_results_to_dataframe(responses, criteria_name):
    """
    Add results to test_results dataframe and include human answers from airs_answers.csv.
    """
    # Extract filenames and results from responses
    filenames = []
    results = []
    ids = []

    for i, resp in enumerate(responses, start=1):
        file_name = resp['file_name']
        response_data = json.loads(resp['response_text'])
        result = response_data.get('Response', 'N/A')

        ids.append(i)
        filenames.append(file_name)
        results.append(result)

    global test_results
    try:
        test_results
    except NameError:
        # Create new dataframe if it doesn't exist
        test_results = pd.DataFrame({
            'id': ids,
            'names': filenames
        })

    test_results[criteria_name] = test_results['id'].map(
            dict(zip(ids, results))
        )

    # Load human answers from airs_answers.csv
    human_answers = pd.read_csv('airs_answers.csv')

    # Add human answer column with _human suffix, mapping by id
    human_column_name = f'{criteria_name}_human'
    test_results[human_column_name] = test_results['id'].map(
        dict(zip(human_answers['id'], human_answers[criteria_name]))
    )

    # Print only relevant columns
    relevant_columns = ['names', criteria_name, human_column_name]
    display(test_results[relevant_columns])

    return test_results

def display_responses(responses):
    """
    Display responses with filename, explanation, and result
    """
    for i, resp in enumerate(responses, 1):
        file_name = resp['file_name']
        response_data = json.loads(resp['response_text'])
        explanation = response_data.get('Explanation', 'N/A')
        result = response_data.get('Response', 'N/A')

        # Display each part
        display(HTML(f"<h3>Response {i}</h3>"))
        display(HTML(f"<strong>File Name:</strong> {file_name}"))
        display(HTML(f"<strong>Explanation:</strong> {explanation}"))
        display(HTML(f"<strong>Result:</strong> {result}"))
        display(HTML("<hr>"))

def create_combined_dataframe(responses_all):
    """
    Creates a DataFrame from responses_all where:
    - Rows are file names
    - Columns are question numbers
    - First column is 'names' containing file names
    - Values are the responses to each question
    - Includes human answers from airs_answers.csv

    Args:
        responses_all: List of dictionaries with 'file_name' and 'response_text' keys.
                      response_text contains multiple JSON objects, one per question.

    Returns:
        DataFrame with file names as rows and questions as columns
    """
    # Dictionary to store data: {file_name: {question_num: response}}
    data_dict = {}
    all_questions = set()

    # Process each file's responses
    for resp in responses_all:
        file_name = resp['file_name']
        response_text = resp['response_text']

        # Initialize dictionary for this file
        if file_name not in data_dict:
            data_dict[file_name] = {}

        # Split response_text into individual JSON objects
        # Each JSON object is on its own lines
        json_objects = []
        current_json = ""
        brace_count = 0

        for line in response_text.split('\n'):
            if line.strip():
                current_json += line + '\n'
                brace_count += line.count('{') - line.count('}')

                if brace_count == 0 and current_json.strip():
                    try:
                        json_obj = json.loads(current_json.strip())
                        json_objects.append(json_obj)
                        current_json = ""
                    except json.JSONDecodeError:
                        continue

        # Extract question numbers and responses
        for json_obj in json_objects:
            question_num = json_obj.get('Question', '')
            response = json_obj.get('Response', 'N/A')

            if question_num:
                data_dict[file_name][question_num] = response
                all_questions.add(question_num)

    # Create DataFrame
    df = pd.DataFrame.from_dict(data_dict, orient='index')

    # Sort columns to ensure questions are in order
    df = df.sort_index(axis=1)

    # Reset index to make file names a column called 'names'
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'names'}, inplace=True)

    # Add 'id' column starting at 1
    df.insert(0, 'id', range(1, len(df) + 1))

    # Load human answers from airs_answers.csv
    human_answers = pd.read_csv('airs_answers.csv')

    # Add human answer columns for each question
    # Convert question number (e.g., "1.1") to column name (e.g., "criteria_1_1")
    for question_num in sorted(all_questions):
        # Convert "1.1" to "criteria_1_1"
        criteria_col_name = f"criteria_{question_num.replace('.', '_')}"
        human_col_name = f"{question_num}_human"

        # Check if the column exists in human_answers
        if criteria_col_name in human_answers.columns:
            # Merge human answers by matching on id column
            df = df.merge(
                human_answers[['id', criteria_col_name]],
                on='id',
                how='left'
            )
            # Rename the merged column to include _human suffix
            df.rename(columns={criteria_col_name: human_col_name}, inplace=True)
        else:
            # If column doesn't exist, fill with N/A
            df[human_col_name] = 'N/A'

    # Reorder columns to interleave questions with their human answers
    # Start with 'id' and 'names' columns
    ordered_columns = ['id', 'names']

    # Add each question followed by its human answer
    for question_num in sorted(all_questions):
        ordered_columns.append(question_num)
        ordered_columns.append(f"{question_num}_human")

    # Reorder the dataframe columns
    df = df[ordered_columns]

    return df