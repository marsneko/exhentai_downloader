import re,requests,a2_modul,front_page
from bs4 import BeautifulSoup as bs
headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
    "Connection":'close'}
cookies={   'igneous':'045d3a87f',
            'ipb_member_id':'3708379',
            'ipb_pass_hash':'93f8d399da142b003efa6cc70561b7c4',
            'sk':'502esnnns8l49o0wleiuu3a2w0do'}
def getapage_list(website):
    list=[]
    result=requests.get(website,headers=headers,cookies=cookies)
    soup=bs(result.content,features='html.parser')
    links=soup.find_all("td",attrs={'class':'gl1e'})
    for i in links:
        try:
            list.append(i.a.attrs['href'])
        except:
            pass
    for i in list:
        print(i)
        alist.append(i)
def getallpage_list(website):
    list=[]
    result=requests.get(website,headers=headers,cookies=cookies)
    soup=bs(result.content,features='html.parser')
    pagenumber=soup.find_all("p",attrs={'class':'ip'})
    regrep=re.compile((r"\D*"))
    print(pagenumber)
    for i in pagenumber:
        print(i.text)
        pagenumber=re.sub(regrep,"",str(i.text))
    pages=int(pagenumber)/25
    getapage_list(website)
    nextpage=""
    if i==0:
        pass
    else:
        for i in range(int(pages)):
            website=soup.find_all('td',onclick="document.location=this.firstChild.href")
            getapage_list(website[len(website)-1].a.attrs['href'])
alist=[]
getallpage_list(input("website"))
f=open('wish_list','a')
f.writelines('\n')
for i in alist:
    f.writelines(i+'\n')
