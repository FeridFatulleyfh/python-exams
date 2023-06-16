#Made By Farid
eded = int(input("Eded daxil edin : "))
cem = 0

while(eded > 0):
    mertebe = eded % 10
    cem = cem + mertebe
    eded = eded //10

print("Cem : " , cem)
