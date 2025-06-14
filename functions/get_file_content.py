# get_file_content.py

import os

def get_file_content(working_directory, file_path):
    MAX_CHARS = 10000

    full_working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(full_working_directory, file_path))
    if not full_path.startswith(full_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(full_path, "r") as f:
            contents = f.read(MAX_CHARS)
            if os.path.getsize(full_path) > MAX_CHARS:
                contents += f'\n[...File "{file_path}" truncated at 10000 characters]\n'
            
            return contents

    except Exception as e:
        return f'Error: {e}'