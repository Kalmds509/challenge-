teks=input("Enter a text: ")
teks=teks.split()
fraz_final=""
for i in teks:
    fraz_final+=i.capitalize()+" "
print(fraz_final)    