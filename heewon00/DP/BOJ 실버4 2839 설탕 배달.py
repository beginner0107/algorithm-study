n= int(input())

d, m = divmod(n,5)

while m%3!=0:
    if d==0:
        print(-1)
        break
    d-=1 ; m+=5

else:
    print(d + m//3)
