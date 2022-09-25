import requests


def get_cookie():
    url = "https://www.emailnator.com/"
    session = requests.Session()
    response = session.get(url)
    cookie = response.cookies.get_dict()

    return cookie
