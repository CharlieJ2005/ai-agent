import os


def get_files_info(working_directory, directory=None):
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
            file_size = os.path.getsize(entry_path)
            result.append(f"- {entry}: file_size={file_size}, is_dir={is_dir}")
        return "\n".join(result)
    except Exception as e:
        return f"Error: {e}"
