import os
import sys


def rename_files(path: str, old: str, new: str) -> None:
    list_of_files = os.listdir(path)
    for file in list_of_files:
        old_file = os.path.join(path, file)
        if os.path.isfile(old_file):
            new_file = os.path.join(path, file.replace(old, new))
            os.rename(old_file, new_file)
    return None


if __name__ == "__main__":
    path, old, new = sys.argv[1:]
    rename_files(path, old, new)
