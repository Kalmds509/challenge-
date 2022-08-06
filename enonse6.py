from ntpath import join
def ranvese(f):
    d="".join(reversed(f))
    d=d.replace(" ","")
    return(d)
print(ranvese("Python se yon langaj pwogramasyon"))