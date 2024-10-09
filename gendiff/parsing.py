"""Parsing files."""

from json import load as json_load
from yaml import safe_load as yaml_load


def get_file_extension(path):
    """Get file extension from path to file.

    Args:
        path: Path to file

    Returns:
        String with extension of file. If extension not exist - emty string
    """
    file_name = path.split('/')[-1]
    split_file_name = file_name.split('.')
    if len(split_file_name) < 2:
        return ''
    return split_file_name[-1]


def get_data(file_path1, file_path2):
    """Get data from files.

    Args:
        file_path1: Path to first file
        file_path2: Path to second file

    Returns:
        Tuple with data from files
    """
    extention = get_file_extension(file_path1)
    if extention == 'json':
        with open(file_path1, 'r') as json_data1:
            first_data = json_load(json_data1)
        with open(file_path2, 'r') as json_data2:
            second_data = json_load(json_data2)
    elif extention in {'yaml', 'yml'}:
        with open(file_path1, 'r') as yaml_data1:
            first_data = yaml_load(yaml_data1)
        with open(file_path2, 'r') as yaml_data2:
            second_data = yaml_load(yaml_data2)
    return (first_data, second_data)
