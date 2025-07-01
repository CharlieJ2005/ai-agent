import os
from google.genai import types


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


def get_files_info(working_directory, directory=None):
    if not directory:
        path = working_directory
    else:
        path = os.path.join(working_directory, directory)
    abs_working_dir = os.path.abspath(working_directory)
    abs_path = os.path.abspath(path)
    if not os.path.commonpath([abs_path, abs_working_dir]) == abs_working_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    try:
        entries = os.listdir(path)
        result = []
        for entry in entries:
            entry_path = os.path.join(path, entry)
            is_dir = os.path.isdir(entry_path)
            file_size = os.path.getsize(entry_path) if not is_dir else 128
            result.append(f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(result)
    except Exception as e:
        return f"Error: {e}"
