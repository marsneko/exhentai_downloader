import requests,re,random,time,os,multiprocessing

from bs4 import BeautifulSoup as bs

def g_photo(website):
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
        result = soup.find_all("div", attrs={'id': 'i7'})
        for i in result:
            try:
                alternative=soup.find_all("img",attrs={'id':'img'})
                for i in alternative:
                    return str(i.attrs['src'])

            except:
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
        print("finish")

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
        result=bs(r.content,features="lxml")
        title_list=result.find("title")
        regrep=re.compile("</?title>")
        for i in title_list:
            return re.sub(regrep,r"",str(i))
        trytime=0

def main(website,pages,startfrom):
    file=title(website)
    file=re.sub("/"," ",file)
    dir="/Users/eric/Downloads/learning/running_bug/img/"+file
    print(dir)
    if not os.path.isdir(dir):
        os.makedirs(dir)
    os.chdir(dir)
    startfrom=int(startfrom)
    current_website=website
    for i in range(int(pages)):
        photo_adress=g_photo(current_website)
        current_website=next_page(current_website)
        p=multiprocessing.Process(target=download,args=(dir,str(startfrom)+".jpg",photo_adress),)
        p.start()
        startfrom=startfrom+1
        time.sleep(float(random.randint(1, 3) / 10))
    p.join()

photo_adress=[]
cookies={   'igneous':'045d3a87f',
            'ipb_member_id':'3708379',
            'ipb_pass_hash':'93f8d399da142b003efa6cc70561b7c4',
            'sk':'502esnnns8l49o0wleiuu3a2w0do'}
if __name__=="__main__":
    trytime=0
    main(input("website\n"), int(input("pages\n")), input("strat from where?\n"))
