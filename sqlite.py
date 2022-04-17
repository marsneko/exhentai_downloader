import a2_modul
status=""
list_=[]
while status!="end":
    status = input('if want to stop then type end')
    if status=="end":
        break
    a=input("website")
    try:
        b=int(input("start-pages"))
        c=int(input("end-pages"))
    except ValueError:
        print("wrong input")
    else:
        if c-b+1>0:
            list_.append([a,c-b+1,b])
        else:
            print("wrong input")
for i in list_:
    a2_modul.main(i[0],i[1],i[2])