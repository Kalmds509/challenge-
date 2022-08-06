"""
Ou gen yon adres ip,ou dwe antre nan yon pot ki ouvri.Ou pa gen anpil tan pou skane tout pot yo,men ou konn pot
ki ouvri a,li egal total to.ut dijit yo ki nan adres ip a,miltipliye pa premye dijit ki nan adres ip an.Nou dwe afiche
pot ki ouvri a le itilizate a fin tape adres ip an
"""
import socket
adresIP=input("Enter the IPadress to know the door that is oppen: ")
try:
    socket.inet_aton(adresIP)
    print("Okay valid IP")
    ad=adresIP.replace(".","")
    s=0
    for k in ad:
        s+=int(k)*int(ad[0])
    print(s)
except socket.error:
    print("Invalid ip,you can't continue")
     
