def read_txt_file(file_path):
    """
    Reads a text file and returns its content as a list of lines.

    :param file_path: Path to the text file.
    :return: List of lines in the text file.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines