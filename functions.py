import os
import json
from openai import OpenAI
from pydantic import BaseModel, Field
from IPython.display import HTML, display
import pandas as pd

def responses_call(document, intro_prompt, criteria_prompt): 
    """
    Calls the language model with the provided document and prompts to generate a response.
    """ 
    response = client.responses.create(
    model='gpt-4o',
    temperature=0,
    instructions=intro_prompt,
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": f"{criteria_prompt}\n"
                },
                {
                    "type": "input_text",
                    "text": f"\nHere is the paper:\n{document}"
                }
            ]
        },
    ]
)
    response_text = response.output_text
    return response_text   

def extract_responses(intro_prompt, criteria_prompt):
    """
    Extracts responses from plain text files in the specified folder using the provided prompts.
    """
    responses = []
    for i, file_name in enumerate(plain_text_files):
        with open(os.path.join(folder, file_name), "r", encoding="utf-8") as f:
            document = f.read()
        response_text = responses_call(document, intro_prompt=intro_prompt, criteria_prompt=criteria_prompt)
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
        result = response_data.get('Reply', 'N/A')

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
        result = response_data.get('Reply', 'N/A')
        
        # Display each part
        display(HTML(f"<h3>Response {i}</h3>"))
        display(HTML(f"<strong>File Name:</strong> {file_name}"))
        display(HTML(f"<strong>Explanation:</strong> {explanation}"))
        display(HTML(f"<strong>Result:</strong> {result}"))
        display(HTML("<hr>"))