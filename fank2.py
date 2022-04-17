import time,a2_modul,front_page

mode=input("choose mode 1'high qulity' 2'low qulity'")
if mode==1 or mode=='high qulity' or 'high':
    mode="high"
else:
    mode="low"

while True:
    f=open("/Users/eric/Downloads/learning/running_bug/wish_list","r")
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
        f=open("/Users/eric/Downloads/learning/running_bug/wish_list","w")
        for i in aontent:
            f.writelines(i)
        f.close()
        f=open("/Users/eric/Downloads/learning/running_bug/finish_list","a")
        f.writelines("")
        f.writelines(place)
        f.close()
        a2_modul.main(front_page.frontpage(front_page.soupmaker(str(place.replace("\n","")))),front_page.pagenumber(front_page.soupmaker(str(place.replace("\n",'')))), int(1))
