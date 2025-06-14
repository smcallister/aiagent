# run_python.py

import os
import subprocess

def run_python_file(working_directory, file_path):
    CMD_TIMEOUT=30

    full_working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(full_working_directory, file_path))
    if not full_path.startswith(full_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    
    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        p = subprocess.run(
            ["python", full_path],
            timeout=CMD_TIMEOUT,
            cwd=os.path.dirname(full_path),
            capture_output=True)
        if len(p.stdout) > 0:
            result = f'STDOUT: {p.stdout.decode()}\n'
        else:
            result = "No output produced.\n"
        
        result += f'STDERR: {p.stderr.decode()}'
        if p.returncode != 0:
            result += f'\nProcess exited with code {p.returncode}'
        
        return result
    
    except Exception as e:
        return f'Error: executing Python file: {e}'