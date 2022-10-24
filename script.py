import requests

# =========================loginAction.html=========================

session = requests.Session()

headers_login = {
    'authority': 'www.10sportal.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'https://www.10sportal.com',
    'pragma': 'no-cache',
    'referer': 'https://www.10sportal.com/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

data_login = {
    'j_username': 'jburns9264', # USERNAME
    'j_password': 'Amogus6969', # PASSWORD
    'rID': 'caswell-tennis-center',
    # 'rememberMe': '1', # irrelevant
}

response = session.post('https://www.10sportal.net/loginAction.html', headers=headers_login, data=data_login)

print(session.cookies.get_dict())

# =========================scheduleDateTimeDiv=========================

headers_schedule = {
    'authority': 'www.10sportal.net',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.10sportal.net/entity/scheduler/index.html',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

params_schedule = {
    'maxAccept': '2',
    'apptTitle': '',
    'etID': '94', # idk what this is, but should probably match the other one
    'listMatchTypeID': '2', # MATCH TYPE: 1 Singles, 2 Doubles
    'apptDate': '10/24/2022', # DATE
    'startTime': '1:00 PM', # START TIME
    'endTime': '2:00 PM', # END TIME
}

response_schedule = session.get('https://www.10sportal.net/entity/scheduler/scheduleDateTimeDiv.cfm', params=params_schedule, headers=headers_schedule)
print(response_schedule)

# =========================availDiv=========================

headers_avail = {
    'authority': 'www.10sportal.net',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.10sportal.net/entity/scheduler/index.html',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

params_avail = {
    'pro': '0',
    'ballMachine': '0',
    'court': '226', # COURT: 225 + N for Crt N where N in [1, 8]
    'apptTitle': '',
    'apptDesc': '',
    'etID': '94',
    'mtID': '2', # MATCH TYPE: 1 Singles, 2 Doubles, needs to match listMatchTypeID above
    'apptComments': '',
    'openTime': '0',
    'editScope': '0',
    '_cf_containerId': 'cf_layoutarea822796061135401',
    '_cf_nodebug': 'true',
    '_cf_nocache': 'true',
    '_cf_clientid': '4A53C07373E938C20B67FDB394B2238C', # TODO not sure what this is for or how to replicate it
    '_cf_rc': '0',
}

response_avail = session.get('https://www.10sportal.net/entity/scheduler/availDiv.cfm', params=params_avail, headers=headers_avail)
print(response_avail)

# =========================scheduler/indexAction.html (submit POST)=========================

headers_submit = {
    'authority': 'www.10sportal.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'https://www.10sportal.net',
    'pragma': 'no-cache',
    'referer': 'https://www.10sportal.net/entity/scheduler/index.html',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

params_submit = {
    'src': 'scheduleEvent',
}

data_submit = {
    'aID': '0',
    'submit': 'Submit',
}

response_submit = session.post('https://www.10sportal.net/entity/scheduler/indexAction.html', params=params_submit, headers=headers_submit, data=data_submit)
print(response_submit)

print('Done')