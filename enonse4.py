def menu():
    print("1-Nan yon enteval,total nonb ki miltip a men ki pa miltip b")
    print("2-Nan yon enteval,total nonb ki miltip b men ki pa miltip a")
    print("3-Nan yon enteval,total nonb ki miltip a ak b")
    print("4-Nan yon enteval,total nonb ki pa miltip ni a ni b")
    a=2
    b=3
    c=0
    chwa=input("Fe chwa")
    if chwa=="1":
        for i in range(1,21):
            if i%a==0 and i%b!=0:
                print(i)
                c+=1
        print("Total nonb ki miltip a ki pa miltip b se:"+str(c))
    elif chwa=="2":
       c=0
       for i in range(1,21):
            if i%b==0 and i%a!=0:
                print(i)
                c+=1
       print("Total nonb ki miltip b ki pa miltip a se:"+str(c))
    elif chwa=="3":
        c=0
        for i in range(1,21):
            if i%a==0 and i%b==0:
                print(i)
                c+=1
        print("Total nonb ki miltip a ak b se :"+str(c))
    elif chwa=="4":
        c=0
        for i in range(1,21):
            if i%a!=0 and i%b!=0:
                print(i)
                c+=1
        print("Total nonb ki pa miltip ni a ni b se :"+str(c))
    

menu()

    