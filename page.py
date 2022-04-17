import requests,re
from bs4 import BeautifulSoup as bs
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15'}
cookies={   'igneous':'045d3a87f',
            'ipb_member_id':'3708379',
            'ipb_pass_hash':'93f8d399da142b003efa6cc70561b7c4',
            'sk':'502esnnns8l49o0wleiuu3a2w0do',
            'u':'3708379-0-f71cly49lea'
}
raw=requests.get("https://exhentai.org/tag/artist:alp",headers=headers,cookies=cookies)
soup=bs(raw.content,features="html.parser")
result=bs.find_all(soup,attrs={'class':'glink'})
regrep=re.compile("<.{1,18}>")
for i in result:
    print(re.sub(regrep,r"",str(i)))
