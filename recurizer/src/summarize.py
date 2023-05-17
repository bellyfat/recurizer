import openai
import os

def file_prompt(fcontents: str):
    system_prompt = """
        You are a helpful coding assistant with the goal of summarizing code source files.
        You're goal is to succinctly summarize the file while preserving the following:
        - The overall structure of the file
        - The overall meaning of the file
        - Individual functions and their purpose
        - Function inputs and outputs
        - Pay special attention to import statements
    """
    code_prompt = f"""The contents of the file are as follows: \n\n{fcontents}"""
    return [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': code_prompt},
    ]


def summarize_file(root:str, fpath: str):
    #given a file path, summarize the file, and append the summary to the .summary file

    try:
        openai.api_key = os.environ['OPENAI_API_KEY']
    except:
        print('OPENAI_API_KEY not found in environment variables')
        return
    
    with open(os.path.join(root, fpath), 'r') as f:
        text = f.read()
    
    summary = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = file_prompt(text),
        temperature = 0.3,
        max_tokens = 150,
    ).choices[0]["message"]["content"]
    full_msg = f"### Summary of {fpath}:\n{summary}\n\n"

    #open the file ".summary" and append the summary to the end of the file
    
    with open(root + '.summary.md', 'a') as f:
        f.write(full_msg)
