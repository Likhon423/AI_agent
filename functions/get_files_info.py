import os
from google.genai import types

def get_files_info(working_directory, directory='.'):
    full_path = os.path.join(working_directory, directory)
    abs_full_path = os.path.abspath(full_path)
    abs_working_dir = os.path.abspath(working_directory)

    if not abs_full_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(abs_full_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        files = os.listdir(abs_full_path)
        files_info = []

        for file in files:
            size = os.path.getsize(os.path.join(abs_full_path, file))
            is_dir = os.path.isdir(os.path.join(abs_full_path, file))
            files_info.append(f"{file}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)