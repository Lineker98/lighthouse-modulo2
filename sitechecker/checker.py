from http.client import HTTPConnection
from urllib.parse import urlparse


def site_is_online(url: str, timeout=10) -> bool:
    """
    Function to test if a website is online

    Args:
        url (str): A list with all the websites urls to be tested.
        timeout (int, optional): The time in seconds to wait for the website
        response. Defaults to 10.

    Raises:
        error: Error associated when trying to connect with the website.

    Returns:
        bool: True if the website is online.
    """
    error = Exception("Was not possible to stablish a connetion.")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error


def display_check_result(result: bool, url: str, error=""):
    """
    Simple function to display the website status.

    Args:
        result (bool): True if the website is online.
        url (str): The website url related to the currently result.
        error (str, optional): The error return by the http connection if
        was not possible to connect with the website. Defaults to "".
    """
    print(f'O status da "{url}" é:', end=" ")
    if result:
        print('"Online!👍"')
    else:
        print(f'"Offline?" 👎 \n  Erro: "{error}"')
