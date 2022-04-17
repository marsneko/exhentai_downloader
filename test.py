import requests,time,re
from bs4 import BeautifulSoup as bs
cookies={   'igneous':'045d3a87f',
            'ipb_member_id':'3708379',
            'ipb_pass_hash':'93f8d399da142b003efa6cc70561b7c4',
            'sk':'502esnnns8l49o0wleiuu3a2w0do',
            'u':'3708379-0-f71cly49lea'}
headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
            }
photos=[]
website="https://exhentai.org/s/61aa381cd6/1809886-60"
try:
    response = requests.get(str(website), headers=headers, cookies=cookies)
    print(response)
finally:
    soup = bs(response.text, features="html.parser")
    result = soup.find_all("img",attrs={'id':'img'})
