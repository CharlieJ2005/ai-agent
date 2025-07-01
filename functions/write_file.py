import os


def write_file(working_directory, file_path, content):
    path = os.path.join(working_directory, file_path)
    abs_working_dir = os.path.abspath(working_directory)
    abs_path = os.path.abspath(path)
    # print(f"\nWorking Directory: {working_directory}\nFile Path: {file_path}\nPath: {path}\nAbsWorkingDirectory: {abs_working_dir}\nAbsPath: {abs_path}")
    if not os.path.commonpath([abs_path, abs_working_dir]) == abs_working_dir:
        f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        with open(abs_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
