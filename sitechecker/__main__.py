import sys
import os
from typing import List, Tuple
import warnings
import click
from multiprocessing.pool import ThreadPool
from csv import reader
import itertools

from sitechecker.checker import site_is_online
from sitechecker.cli import display_check_result

warnings.filterwarnings("always", category=ResourceWarning)

@click.command()
@click.option("--urls", required=False, multiple=True, type=str, help="The web site url you want to check.")
@click.option("-f", "--file", type=str, default='', required=False, help="The path to the file with all urls to be tested.")
@click.option("--multiprocessing", default=False, is_flag=True, required=False, help="Add paralelism to check the websites. In case you would like to verify many websites")
def main(urls: Tuple[str], file: str, multiprocessing: bool):
    """
    Main function called when run the package as a module. 
    This function get all the arguments by cli and show the result
    for each website calling other specific functions.
    """
    urls = list(urls)
    urls = _get_urls(urls, file)
    if not urls:
        print("Por favor, insira a URL!")
        sys.exit(1)

    if multiprocessing:
        with ThreadPool() as pool:
            items = [(item,) for item in urls]
            for url in pool.map(_site_check, items):
                continue
    else:
        _site_check(urls)

def flatten(list_object: List) -> List[str]:
    """_summary_

    Args:
        list_object (List): _description_

    Returns:
        List[str]: _description_
    """
    flat_list = itertools.chain.from_iterable(list_object)
    flat_list = list(flat_list)
    return flat_list


def _get_urls(urls: Tuple[str], file: str) -> List:
    """
    Function to read the urls and put together with the urls written in 
    the file, if it exists ou have been passed by the user.

    Args:
        args (Namespace): The arguments passed by the user in cli command.

    Returns:
        List: A list with all the urls.
    """

    if file:
        urls += _get_urls_from_file(file)
    return urls


def _get_urls_from_file(path_to_file: str) -> List:
    """
    Function to read all the urls present in the file specified by the user

    Args:
        path_to_file (str): The full or relative path to the file with the urls.

    Returns:
        List: A list with all the urls in the file.
    """
    if os.path.isfile(path_to_file):
        with open(path_to_file, 'r') as f:
            urls = list(reader(f, delimiter=","))
            urls = flatten(urls)
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