
import string
alfa="abcdefghijklmnopqrstuvwxyz"
# a="<7y >4k >3r >3q >2c >2p" 
a="<7m >8j <7v >7g >6n >2c <1o <9m"
k=a.split(" ")
mot=""
for l in k:
    if l[0]=="<":
        idx=alfa.index(l[2])-int(l[1])
    if l[0]==">":
        idx=alfa.index(l[2])+int(l[1])
    mot+=alfa[idx]
print(mot)   
    
   
    



          
            



    





