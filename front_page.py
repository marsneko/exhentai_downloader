from bs4 import BeautifulSoup as bs
import requests,re,a2_modul
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',"Connection":'close'}
cookies={   'igneous':'045d3a87f',
            'ipb_member_id':'3708379',
            'ipb_pass_hash':'93f8d399da142b003efa6cc70561b7c4',
            'sk':'502esnnns8l49o0wleiuu3a2w0do',
            'u':'3708379-0-f71cly49lea'
}
def soupmaker(website):
    r = requests.get(str(website), headers=headers, cookies=cookies)
    result = bs(r.content, features='html.parser')
    return result

def frontpage(result):
    page=result.find("div",attrs={'class':"gdtl"})
    for i in page:
        try:
            print(i.attrs['href'])
            return(i.attrs['href'])

        except:
            pass
def pagenumber(result):
    patten=re.compile(r" pages")
    page=result.find_all('td',attrs={'class':'gdt2'})
    for i in page:
        if 'page' in str(i):
            a=re.sub(patten,"",i.text)
            return int(a)

