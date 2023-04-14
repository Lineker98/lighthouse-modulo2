import argparse

def read_user_cli_args() -> argparse.Namespace:
    """
    Function to get all the user arguments written in cli command (website urls)

    Returns:
        argparse.Namespace: A Namespace with a list of all urls gotten.
    """

    parser = argparse.ArgumentParser(
        prog="sitechecker", description="Teste a disponibilidade de uma URL"
    )

    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Insira um ou mais URLs"
    )
    return parser.parse_args()

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