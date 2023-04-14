import sys
import os
from typing import List
from argparse import Namespace
import warnings

from sitechecker.checker import site_is_online
from sitechecker.cli import display_check_result, read_user_cli_args

warnings.filterwarnings("always", category=ResourceWarning)

def main():
    """
    Main function called when run the package as a module. 
    This function get all the arguments by cli and show the result
    for each website calling other specific functions.
    """
    user_args = read_user_cli_args()
    urls = _get_urls(user_args)
    if not urls:
        print("Por favor, insira a URL!")
        sys.exit(1)
    _site_check(urls)


def _get_urls(args: Namespace) -> List:
    """
    Function to read the urls and put together with the urls written in 
    the file, if it exists ou have been passed by the user.

    Args:
        args (Namespace): The arguments passed by the user in cli command.

    Returns:
        List: A list with all the urls.
    """
    urls = args.urls
    if args.file:
        urls += _get_urls_from_file(args.file)
    return urls


def _get_urls_from_file(path_to_file: str) -> List:
    """
    Function to read all the urls present in the file specified by the user

    Args:
        path_to_file (str): The full or relative patj to the file with the urls.

    Returns:
        List: A list with all the urls in the file.
    """
    if os.path.isfile(path_to_file):
        with open(path_to_file) as f:
            urls = f.readlines()
            urls = list(map(lambda url: url.strip(), urls))
            if urls:
                return urls
            warnings.warn("The file is empty, there are no urls!", ResourceWarning)
    else:
        print("Error: file not found")
    return []



def _site_check(urls: List[str]):
    """
    Check if each website is online.

    Args:
        urls (List[str]): A List with all the urls to be checked.
    """

    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

if __name__ == "__main__":
    main()