import time,a2_modul,front_page,os
mode=input("choose mode(high/low)")
gape=input("choose how many page should use low qulity")
limit=input("excees how many page should be give up")
gape=int(gape)
limit=int(limit)

while True:
    os.chdir("/Users/eric/Documents/learning/running_bug/img")
    f=open("/Users/eric/Documents/learning/running_bug/wish_list_1","r")
    f.seek(0)
    place=f.readline()
    mouse=f.tell()
    if place=="":
        f.close()
        time.sleep(10)
    else:
        f.seek(int(mouse))
        aontent=[]
        for i in f.readlines():
            aontent.append(i)
        f.close()
        f=open("/Users/eric/Documents/learning/running_bug/wish_list_1","w")
        for i in aontent:
            f.writelines(i)
        f.close()
        f=open("/Users/eric/Documents/learning/running_bug/finish_list","a")
        f.writelines("")
        f.writelines(place)
        f.close()
        page_=int(front_page.pagenumber(front_page.soupmaker(str(place.replace("\n",'')))))
        if page_>limit:
            continue
        if page_>int(gape):
            mode="low"
        a2_modul.main(front_page.frontpage(front_page.soupmaker(str(place.replace("\n","")))),front_page.pagenumber(front_page.soupmaker(str(place.replace("\n",'')))), int(1),mode=mode)
