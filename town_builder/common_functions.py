import yaml
import os

def import_yaml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def find_files_by_extension(directory, extension):
    """
    Find all files with a specific file extension in a directory.

    Args:
    directory (str): The directory path to search for files.
    extension (str): The file extension (e.g., '.txt', '.jpg') to search for.

    Returns:
    list: A list of file paths that match the given extension.
    """
    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                matching_files.append(os.path.join(root, file))
    return matching_files