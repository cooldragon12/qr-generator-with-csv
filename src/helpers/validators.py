from os import path
def check_if_file_exists(file_location):
    """
    Check if the file exists
    :param file_location: The location of the file
    :return: True if the file exists, False if not
    """
    return path.exists(file_location)