import colorama
from colorama import Fore, Style
import os
import sys
from pathlib import Path


def visualize_directory_tree(path):
    """
    Recursively traverses the directory tree and prints the names of directories and files,
    using different colors for directories and files.

    Args:
        path (str): The path to the directory to visualize.
    """

    dir_path = Path(path)

    if not dir_path.exists():
        print(f"Error: Directory '{dir_path}' does not exist.")
        return

    if not dir_path.is_dir():
        print(f"Error: '{dir_path}' is not a directory.")
        return

    for item in dir_path.iterdir():
        if item.is_dir():
            print(Fore.BLUE + Style.BRIGHT + f"[DIR] {item.name}")
            visualize_directory_tree(item)
        else:
            print(Fore.GREEN + f"    {item.name}")


visualize_directory_tree(r"C:\Users\Admin\PycharmProjects\goit-pycore-hw-04+")