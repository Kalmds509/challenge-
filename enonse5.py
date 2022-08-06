chenn="5 45 123 12"
chenn_nan=chenn.split(" ")
pwod=1
for i in chenn_nan:
    s=0
    for k in range(len(i)):
        s+=int(i[k])
    pwod*=s
print(pwod)

     
        
        
        