import os


def get_files_info(working_directory, directory="."):
    abspath = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(abspath, directory))
    valid_target_dir = os.path.commonpath([abspath, full_path]) == abspath
    if os.path.isdir(full_path):
        raise Exception(f'Error: "{directory}" is not a directory')
    if not valid_target_dir:
        raise Exception(
            f'Error: Cannot list "{
                directory
            }" as it is outside the permitted working directory'
        )
