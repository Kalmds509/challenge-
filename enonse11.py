lis=[5,4,0,15,57,8,12]
pi_piti=lis[0]
pi_gran=lis[0]
for i in lis[1:]:
    if i<pi_piti:
        pi_piti=i
    elif i>pi_gran:
        pi_gran=i
print(pi_piti,pi_gran)
