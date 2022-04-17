from bs4 import BeautifulSoup as bs
import requests,lxml,re
def title(website):
    r=requests.get(website,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15'})
    result=bs(r.content,features="lxml")
    title=result.find("title")
    regrep=re.compile("</?title>")
    for i in title:
        return re.sub(regrep,r"",str(i))
print(title("https://e-hentai.org/s/7a8d7b7740/1835694-1"))