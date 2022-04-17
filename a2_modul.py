import requests,re,random,time,os

from bs4 import BeautifulSoup as bs

def g_photo(website,mode):
    global trytimes
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15'}
    try:
        response = requests.get(str(website),headers=headers,cookies=cookies)
        trytimes=0
    except :

        print('error')
        time.sleep(3)
        g_photo(website)
        trytimes=trytimes+1
    else:
        soup = bs(response.text, features="html.parser")
        
        # highqulity
        if mode=="high":
            try:
                result = soup.find_all("div", attrs={'id': 'i7'})
                for i in result:
                    b = str(bs.get(i.a, "href"))
                    return b
            except:
                alternative = soup.find_all("img", attrs={'id': 'img'})
                for i in alternative:
                    return str(i.attrs['src'])
        #low qulity
        else:
            try:
                alternative = soup.find_all("img", attrs={'id': 'img'})
                for i in alternative:
                    return str(i.attrs['src'])
            except:
                result = soup.find_all("div", attrs={'id': 'i7'})
                for i in result:
                    b = str(bs.get(i.a, "href"))
                    return b

        
        trytimes = 0
def next_page(website):
    global trytime
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
    "Connection":'close'}
    try:
        response = requests.get(str(website), headers=headers, cookies=cookies)
        trytime=0
    except :
        if trytime>10:
            breakpoint()
        print("error")
        time.sleep(3)
        next_page(website)
        trytime=trytime+1
        print(trytime)
    else:
        soup = bs(response.text, features="html.parser")
        result = soup.find("a", id="next")
        nextpage =result.get('href')
        trytime=0
        return nextpage

"""def ranger_weber(website,pages):
    for i in range(int(pages)):
        g_photo(website)
        website=nextpage"""

def download(dir,name,img):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
    "Connection":'close'}
    if not os.path.isdir(dir):
        os.makedirs(str(dir))
    os.chdir(dir)
    global trytime
    try:
        r=requests.get(img,headers=headers,cookies=cookies,stream=True)
        trytime=0
    except:
        if trytime>10:
            breakpoint()
        print('error')
        time.sleep(3)
        download(dir,name,img)
        trytime=trytime+1
    else:
        f=open(str(name),"wb+")
        f.write(r.content)
        trytime=0

def title(website):
    global trytime
    try:

        r=requests.get(website,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',"Connection":'close'},cookies=cookies)
        trytime=0
    except :
        if trytime>10:
            breakpoint()
        print('error')
        time.sleep(3)
        title(website)
        trytime=trytime+1
    else:
        result=bs(r.content,features="html.parser")
        title_list=result.find("title")
        regrep1=re.compile("</?title>")
        regrep2=re.compile("/")
        for i in title_list:
            text=re.sub(regrep1,r"",str(i))
            return re.sub(regrep2,"",text)
        trytime=0

def main(website,pages,startfrom,mode="low"):
    dir =str(os.getcwd()) + "/img/" + title(website)
    startfrom=int(startfrom)
    current_website=website
    for i in range(int(pages)):
        photo_adress=g_photo(current_website,mode)
        current_website=next_page(current_website)
        download(dir,str(startfrom)+".jpg",photo_adress)
        startfrom=startfrom+1

photo_adress=[]
cookies={   'igneous':'045d3a87f',
            'ipb_member_id':'3708379',
            'ipb_pass_hash':'93f8d399da142b003efa6cc70561b7c4',
            'sk':'502esnnns8l49o0wleiuu3a2w0do'}
if __name__=="__main__":
    trytime=0
    main(input("website\n"), int(input("pages\n")), input("strat from where?\n"), mode=input("mode\n"))
