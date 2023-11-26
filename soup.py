import requests
from bs4 import BeautifulSoup

import requests

headers = {
    'authority': 'api.sofascore.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': 'W/"4db8d0c803"',
    'origin': 'https://www.sofascore.com',
    'referer': 'https://www.sofascore.com/',git 
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36 Edg/118.0.2088.76',
}


headers['If-Modified-Since'] = 'Sun, 26 Nov 2023 4:36:00 GMT'

response = requests.get('https://api.sofascore.com/api/v1/event/11352385/statistics', headers=headers)


statistics = response.json()

for x in statistics['statistics']:
    corner_kicks_home = x['groups'][3]['statisticsItems'][0]['homeValue']
    corner_kicks_away = x['groups'][3]['statisticsItems'][0]['awayValue']
    print(corner_kicks_home)
    print('-'*100)


