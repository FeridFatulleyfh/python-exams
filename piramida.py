sira=int(input())
if sira <65:
    for i in range(sira):
        print(" "*(sira-i-1) + "*"*(2*i+1))
else:
    print("Daha kicik reqem daxil edin")
