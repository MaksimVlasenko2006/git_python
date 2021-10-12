a=int(input("Pologil-"))
b=int(input("Procent-"))
d=int(input("Month-"))
if d>12:
    k=d//12
    for i in range(k):
        a=a+a*(b/100)
        print(a)
else:
    print(a)
