import os


def get_file_content(working_directory, file_path):
    path = os.path.join(working_directory, file_path)
    abs_working_dir = os.path.abspath(working_directory)
    abs_path = os.path.abspath(path)
    # print(f"\nWorking Directory: {working_directory}\nFile Path: {file_path}\nPath: {path}\nAbsWorkingDirectory: {abs_working_dir}\nAbsPath: {abs_path}")
    if not os.path.commonpath([abs_path, abs_working_dir]) == abs_working_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        MAX_CHARS = 10000
        with open(abs_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(f.read()) > MAX_CHARS:
                file_content_string += (f'[...File "{file_path}'' truncated at 10000 characters]')
            return file_content_string
    except Exception as e:
        return f"Error: {e}"
