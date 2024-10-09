"""Generate difference between two json or yaml files.

Takes paths to files as input and
outputs the difference between them as string.
"""

from gendiff.parsing import get_data


def bool_to_lowercase(input_value):
    """If input value is boolean convert it to string in lowercase.

    Args:
        input_value: Any value

    Returns:
        String in lowercase if input is boolean, in other case input_value
    """
    if isinstance(input_value, bool):
        return str(input_value).lower()
    return input_value


def generate_diff(file_path1, file_path2):
    """Generate difference between two json or yaml files.

    Args:
        file_path1: Path to first file
        file_path2: Path to second file

    Returns:
        String contains difference between two files located at paths
        in file_path1 and file_path2
    """
    first_data, second_data = get_data(file_path1, file_path2)
    keys = first_data.keys() | second_data.keys()
    keys = sorted(keys)
    diff_list = ['{']
    for key in keys:
        if key not in first_data:
            second_data_value = bool_to_lowercase(second_data[key])
            diff_list.append(f'  + {key}: {second_data_value}')
        elif key not in second_data:
            first_data_value = bool_to_lowercase(first_data[key])
            diff_list.append(f'  - {key}: {first_data_value}')
        elif first_data[key] == second_data[key]:
            first_data_value = bool_to_lowercase(first_data[key])
            diff_list.append(f'    {key}: {first_data_value}')
        else:
            first_data_value = bool_to_lowercase(first_data[key])
            second_data_value = bool_to_lowercase(second_data[key])
            diff_list.append(f'  - {key}: {first_data_value}')
            diff_list.append(f'  + {key}: {second_data_value}')
    diff_list.append('}')
    return '\n'.join(diff_list)
