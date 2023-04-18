import argparse
import click


def display_check_result(result: bool, url: str, error=""):
    """
    Simple function to display the website status.

    Args:
        result (bool): True if the website is online.
        url (str): The website url related to the currently result.
        error (str, optional): The error return by the http connection if
        was not possible to connect with the website. Defaults to "".
    """
    print(f'Os status da "{url}" é:', end =" ")
    if result:
        print('"Online!👍"')
    else:
        print(f'"Offline?" 👎 \n  Erro: "{error}"')