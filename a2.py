import requests,re,random,time,os

from bs4 import BeautifulSoup as bs

def g_photo(website):
    global nextpage
    photos=[]
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15'}
    try:
        response = requests.get(str(website),headers=headers,cookies=cookies)
    except ConnectionError:
        time.sleep(3)
        g_photo(website)
    finally:
        soup = bs(response.text, features="html.parser")
        result = soup.find_all("img", attrs={'id': 'img'})
        for i in result:
            return str(bs.get(i,"src"))
def next_page(website):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15'}
    try:
        response = requests.get(str(website), headers=headers, cookies=cookies)
    except ConnectionError:
        time.sleep(3)
        next_page(website)
    finally:
        soup = bs(response.text, features="html.parser")
        result = soup.find("a", id="next")
        nextpage =result.get('href')
        return nextpage

"""def ranger_weber(website,pages):
    for i in range(int(pages)):
        g_photo(website)
        website=nextpage"""

def download(dir,name,img):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15'}
    if not os.path.isdir(dir):
        os.mkdir(str(dir))
    os.chdir(dir)
    try:
        r=requests.get(img,headers=headers,cookies=cookies)
    except ConnectionError:
        time.sleep(3)
        download(dir,name,img)
    else:
        f=open(str(name),"wb+")
        f.write(r.content)

def main(website,pages,startfrom):
    dir = "/Users/eric/Downloads/learning/running_bug/img/" + title(website)
    a=int(startfrom)
    current_website=website
    for i in range(int(pages)):
        photo_adress=g_photo(current_website)
        current_website=next_page(current_website)
        download(dir,str(a)+".jpg",photo_adress)
        a=a+1
        '''time.sleep(float(random.randint(1, 3) / 10))'''
def title(website):
    r=requests.get(website,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15'},cookies=cookies)
    result=bs(r.content,features="lxml")
    title=result.find("title")
    regrep=re.compile("</?title>")
    for i in title:
        return re.sub(regrep,r"",str(i))





photo_adress=[]
cookies={   'igneous':'045d3a87f',
            'ipb_member_id':'3708379',
            'ipb_pass_hash':'93f8d399da142b003efa6cc70561b7c4',
            'sk':'502esnnns8l49o0wleiuu3a2w0do',
            'u':'3708379-0-f71cly49lea'}
main(input("website\n"),int(input("pages\n")),input("strat from where?\n"))