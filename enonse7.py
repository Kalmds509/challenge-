#Ranplase tou let ki devan yon voyel pa yon *
teks=input("Antre yon teks: ")
teks=teks.strip()
voyel="aeiouyAEIOUY"
for i in range(len(teks)):
    if teks[i] in voyel:
        teks=teks.replace(teks[i-1],"*")
print(teks)
