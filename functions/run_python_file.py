import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    abs_full_path = os.path.abspath(full_path)
    abs_working_dir = os.path.abspath(working_directory)

    if not abs_full_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_full_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        completed_process = subprocess.run(
            ['python3', abs_full_path] + args,
            capture_output=True,
            text=True,
            cwd=working_directory,
            timeout=30
        )

        output_lines = []
        if completed_process.stdout:
            output_lines.append(f"STDOUT: {completed_process.stdout}")
        if completed_process.stderr:
            output_lines.append(f"STDERR: {completed_process.stderr}")
        if completed_process.returncode != 0:
            output_lines.append(f'Process exited with code {completed_process.returncode}')

        if not output_lines:
            return "No output produced."
        
        return "\n".join(output_lines)
    
    except subprocess.TimeoutExpired:
        return f'Error: Execution of "{file_path}" timed out after 30 seconds.'
    except Exception as e:
        return f"Error: executing Python file: {e}"
    


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)