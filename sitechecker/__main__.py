import sys

from asyncore import read
from sitechecker.checker import site_is_online
from sitechecker.cli import display_check_result, read_user_cli_args
from typing import List

def main():
    """
    Main function called when run the package as a module. 
    This function get all the arguments by cli and show the result
    for each website calling other specific functions.
    """
    user_args = read_user_cli_args()
    urls = user_args.urls
    if not urls:
        print("Por favor, insira a URL!")
        sys.exit(1)
    _site_check(urls)

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