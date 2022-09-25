try:
    import requests
except:
     import os 
     os.system("pip install requests")
     import requests
import json
from core.token_parser import *
from core.gen_email import *
from core.text_parser import *


def get_email_response():
    print("Generating mail address.....")
    print("Please wait :)")
    data_cookie = json.loads(json.dumps(get_cookie()))
    xsrf_token = str(data_cookie['XSRF-TOKEN']).replace('%3D', "=")
    session_token = data_cookie['gmailnator_session']
    burp0_url = "https://www.emailnator.com:443/message-list"
    email = gen_email()
    burp0_cookies = {"XSRF-TOKEN": f"{xsrf_token}",
                     "gmailnator_session": f"{session_token}"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "X-Requested-With": "XMLHttpRequest", "Content-Type": "application/json",
                     "X-Xsrf-Token": f"{xsrf_token}", "Origin": "https://www.emailnator.com", "Referer": "https://www.emailnator.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
    burp0_json = {"email": f"{email}"}
    print(f'Email : {email}')
    print('\n\nWating For Msg........')
    while True:
        response = requests.post(burp0_url, headers=burp0_headers,
                                 cookies=burp0_cookies, json=burp0_json).json()
        messges_id = response['messageData']
        total_messeges = len(messges_id)
        for i in range(total_messeges):

            if len(str(messges_id[i]['messageID'])) > 12:
                messges_id_base = messges_id[i]['messageID']
                with open('temp_id.txt', 'r') as read_file:
                    if messges_id_base not in str(read_file.readlines()):
                       
                        print('Message Found!')
                        print('Mailbox Address : http://localhost:8000/')
                        with open('temp_id.txt','a') as w:
                             w.write(messges_id_base+"\n")
                             w.close()
                        subject_text = messges_id[i]['subject']
                        from_email = messges_id[i]['from']
                        burp0_url_email = "https://www.emailnator.com:443/message-list"
                        burp0_json_email = {"email": f"{email}",
                                            "messageID": f"{messges_id_base}"}
                        message = requests.post(
                            burp0_url_email, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json_email)
                        with open('index.html', 'a+', encoding='utf-8') as w:
                            if str(response) not in str(w.readlines()):

                                w.write(message.text+"\n")
                            w.close()
