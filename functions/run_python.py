import os
import subprocess

def run_python_file(working_directory, file_path):
    path = os.path.join(working_directory, file_path)
    abs_working_dir = os.path.abspath(working_directory)
    abs_path = os.path.abspath(path)
    # print(f"\nWorking Directory: {working_directory}\nFile Path: {file_path}\nPath: {path}\nAbsWorkingDirectory: {abs_working_dir}\nAbsPath: {abs_path}")
    if not os.path.commonpath([abs_path, abs_working_dir]) == abs_working_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(
            ["python3", abs_path],
            timeout=30,
            capture_output=True,
            cwd=abs_working_dir
        )
        output = []
        output.append(f"STDOUT: {result.stdout}")
        output.append(f"STDERR: {result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not output:
            return "No output produced."
        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"