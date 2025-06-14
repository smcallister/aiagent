# get_files_info.py

import os

def get_file_info(directory, file_name):
    file_path = os.path.join(directory, file_name)
    return f'{file_name}: file_size={os.path.getsize(file_path)} bytes, is_dir={not os.path.isfile(file_path)}'


def get_files_info(working_directory, directory=None):
    full_working_directory = os.path.abspath(working_directory)
    full_directory = os.path.abspath(os.path.join(full_working_directory, directory))
    if not full_directory.startswith(full_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(full_directory):
        return f'Error: "{directory}" is not a directory'

    return "\n".join(list(map(lambda file_name: get_file_info(full_directory, file_name), os.listdir(full_directory))))