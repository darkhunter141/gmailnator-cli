import requests
import json
from core.token_parser import *


def gen_email():
    data_cookie = json.loads(json.dumps(get_cookie()))
    xsrf_token = str(data_cookie['XSRF-TOKEN']).replace('%3D', "=")
    session_token = data_cookie['gmailnator_session']

    burp0_url = "https://www.emailnator.com:443/generate-email"
    burp0_cookies = {"XSRF-TOKEN": f"{xsrf_token}",
                     "gmailnator_session": f"{session_token}"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "X-Requested-With": "XMLHttpRequest", "Content-Type": "application/json",
                     "X-Xsrf-Token": f"{xsrf_token}", "Origin": "https://www.emailnator.com", "Referer": "https://www.emailnator.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
    burp0_json = {"email": ["dotGmail"]}
    response = requests.post(burp0_url, headers=burp0_headers,
                             cookies=burp0_cookies, json=burp0_json).json()

    email = response['email'][0]
    return email
